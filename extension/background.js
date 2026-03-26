// ─── Config ────────────────────────────────────────────────────────────────
const API_BASE = "http://localhost:8000";
const INJECT_FLAG = "__circleSearchInjected";

// ─── Helpers ───────────────────────────────────────────────────────────────

/**
 * Safely send a message to a tab. Never throws — logs silently if the tab
 * is gone or the content script isn't ready.
 */
async function safeSendMessage(tabId, payload) {
  try {
    await chrome.tabs.sendMessage(tabId, payload);
  } catch (e) {
    console.warn(`[CircleSearch] Could not message tab ${tabId}:`, e.message);
  }
}

function showNotification(title, message) {
  chrome.notifications.create({
    type: "basic",
    iconUrl: "icons/icon48.png",
    title,
    message,
    priority: 1,
  });
}

/**
 * Check whether content.js has already been injected into a tab.
 * Returns true/false. Never throws.
 */
async function isAlreadyInjected(tabId) {
  try {
    const [result] = await chrome.scripting.executeScript({
      target: { tabId },
      func: () => !!window.__circleSearchInjected,
    });
    return result?.result === true;
  } catch {
    return false; // treat unknown state as "not injected"
  }
}

// ─── Action click → inject content script ──────────────────────────────────

chrome.action.onClicked.addListener(async (tab) => {
  // Guard: some pages (chrome://, the Web Store, etc.) block scripting entirely
  if (
    !tab.id ||
    !tab.url ||
    tab.url.startsWith("chrome://") ||
    tab.url.startsWith("chrome-extension://") ||
    tab.url.startsWith("https://chrome.google.com/webstore")
  ) {
    showNotification(
      "Circle Search AI",
      "This page is restricted. Try on a regular website."
    );
    return;
  }

  try {
    // ── Deduplicate injection ──────────────────────────────────────────────
    const alreadyInjected = await isAlreadyInjected(tab.id);

    if (!alreadyInjected) {
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"],
      });
    }

    // executeScript is fully awaited before we message — no setTimeout needed
    await safeSendMessage(tab.id, { action: "open_overlay" });
  } catch (err) {
    console.error("[CircleSearch] Injection failed:", err);
    showNotification(
      "Circle Search AI",
      "Could not activate on this page. It may be restricted."
    );
  }
});

// ─── Message listener → capture screen & call backend ──────────────────────

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action !== "capture_screen") return; // ignore unrelated messages

  const tabId = sender?.tab?.id;
  const windowId = sender?.tab?.windowId;

  if (!tabId || !windowId) {
    console.warn("[CircleSearch] capture_screen received with no sender tab.");
    return;
  }

  // Run async work inside an IIFE so we can use await cleanly
  (async () => {
    try {
      // ── Capture the visible tab ──────────────────────────────────────────
      const dataUrl = await new Promise((resolve, reject) => {
        chrome.tabs.captureVisibleTab(windowId, { format: "png" }, (url) => {
          if (chrome.runtime.lastError) {
            reject(new Error(chrome.runtime.lastError.message));
          } else {
            resolve(url);
          }
        });
      });

      // ── Convert data URL → Blob → FormData ──────────────────────────────
      const blob = await (await fetch(dataUrl)).blob();
      const formData = new FormData();
      formData.append("image", blob, "screenshot.png");

      // ── POST to backend ──────────────────────────────────────────────────
      const response = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Backend returned HTTP ${response.status}`);
      }

      const data = await response.json();

      // ── Send result back to content script ──────────────────────────────
      await safeSendMessage(tabId, { action: "display_result", data });
    } catch (e) {
      console.error("[CircleSearch] Capture/predict error:", e);
      await safeSendMessage(tabId, {
        action: "display_error",
        message: "Something went wrong. Please try again.",
      });
    }
  })();

  // We respond via safeSendMessage above, not via sendResponse,
  // so we do NOT return true here (avoids misleading open channel).
});