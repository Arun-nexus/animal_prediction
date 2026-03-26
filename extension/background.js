const API_BASE = "http://localhost:8000";
const INJECT_FLAG = "__circleSearchInjected";

// ─── Helpers ─────────────────────────────────────────

async function safeSendMessage(tabId, payload) {
  if (!tabId) return;
  try {
    await chrome.tabs.sendMessage(tabId, payload);
  } catch (e) {
    // Tab closed ya content script ready nahi — silently ignore
    console.warn(`[CircleSearch] Tab ${tabId} message failed:`, e.message);
  }
}

function showNotification(title, message) {
  // Chrome extension notifications mein iconUrl ke liye sirf
  // extension ke andar ki files kaam karti hain — data: URLs nahi.
  // Isliye hum ek guaranteed fallback PNG use kar rahe hain.
  const iconUrl = chrome.runtime.getURL("icons/icon128.png");

  // Pehle icon ke saath try karo
  chrome.notifications.create(
    {
      type: "basic",
      iconUrl,
      title,
      message,
      priority: 1,
    },
    (notifId) => {
      if (chrome.runtime.lastError) {
        // Icon nahi mila — bina icon ke dobara try karo (1x1 transparent PNG)
        chrome.notifications.create({
          type: "basic",
          iconUrl:
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
          title,
          message,
          priority: 1,
        });
      }
    }
  );
}

async function isAlreadyInjected(tabId) {
  try {
    const [result] = await chrome.scripting.executeScript({
      target: { tabId },
      func: (flag) => !!window[flag],
      args: [INJECT_FLAG],
    });
    return result?.result === true;
  } catch {
    // executeScript fail hua (restricted page etc.) — safe false return
    return false;
  }
}

// ─── Tab URL Validation ───────────────────────────────

function isRestrictedUrl(url) {
  if (!url) return true;
  const restricted = [
    "chrome://",
    "chrome-extension://",
    "edge://",
    "about:",
    "data:",
    "javascript:",
    "devtools://",
  ];
  return restricted.some((prefix) => url.startsWith(prefix));
}

// ─── Action Click ─────────────────────────────────────

chrome.action.onClicked.addListener(async (tab) => {
  console.log("[CircleSearch] Icon clicked:", tab?.url);

  // Tab ID check
  if (!tab?.id) {
    console.warn("[CircleSearch] No tab ID found.");
    return;
  }

  // Restricted page check
  if (isRestrictedUrl(tab.url)) {
    console.warn("[CircleSearch] Restricted URL:", tab.url?.substring(0, 60));

    let msg = "Circle Search AI yahan kaam nahi karta.";

    if (tab.url?.startsWith("data:")) {
      msg = "Koi image/file directly browser mein khuli hai. Kisi website par jaake try karo.";
    } else if (tab.url?.startsWith("chrome://") || tab.url?.startsWith("edge://")) {
      msg = "Browser ke internal pages par extension use nahi ho sakta.";
    } else if (tab.url?.startsWith("chrome-extension://")) {
      msg = "Extension pages par Circle Search kaam nahi karta.";
    } else if (!tab.url) {
      msg = "Page load nahi hua. Thoda wait karke dobara try karo.";
    }

    showNotification("⚠️ Circle Search AI", msg);
    return;
  }

  try {
    const injected = await isAlreadyInjected(tab.id);
    console.log("[CircleSearch] Already injected?", injected);

    if (!injected) {
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"],
      });
      console.log("[CircleSearch] content.js injected successfully.");

      // Inject hone ke baad thoda wait — content script ko ready hone do
      await new Promise((resolve) => setTimeout(resolve, 150));
    }

    await safeSendMessage(tab.id, { action: "open_overlay" });

  } catch (err) {
    console.error("[CircleSearch] Injection failed:", err);
    showNotification(
      "Circle Search AI",
      "Extension load nahi ho saki. Page refresh karke try karo."
    );
  }
});

// ─── Message Listener (Capture + API) ────────────────

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  // Sirf capture_screen handle karo
  if (request.action !== "capture_screen") return false;

  const tabId = sender?.tab?.id;
  const windowId = sender?.tab?.windowId;

  if (!tabId || !windowId) {
    console.warn("[CircleSearch] capture_screen: tabId/windowId missing.");
    return false;
  }

  // Async flow — return true zaroori hai
  (async () => {
    try {
      // ── Step 1: Screenshot lo ──
      const dataUrl = await captureTab(windowId);

      // ── Step 2: Crop karo agar cropRect mila ──
      const croppedUrl = request.cropRect
        ? await cropImage(dataUrl, request.cropRect)
        : dataUrl;

      // ── Step 3: Blob banao ──
      const blob = await dataUrlToBlob(croppedUrl);

      // ── Step 3: FormData banao ──
      const formData = new FormData();
      formData.append("image", blob, "screenshot.png");

      // Crop coordinates agar mile toh bhejo
      if (request.cropRect) {
        formData.append("cropRect", JSON.stringify(request.cropRect));
      }

      // ── Step 4: Backend call ──
      const data = await callBackend(formData);

      // ── Step 5: Result content script ko bhejo ──
      await safeSendMessage(tabId, {
        action: "display_result",
        data,
      });

    } catch (e) {
      console.error("[CircleSearch] Pipeline error:", e);

      // User-friendly error messages
      let userMsg = "Kuch galat ho gaya. Dobara try karo.";

      if (e.message?.includes("aborted") || e.message?.includes("timeout")) {
        userMsg = "Backend respond nahi kar raha (timeout). Server check karo.";
      } else if (e.message?.includes("fetch") || e.message?.includes("Failed to fetch")) {
        userMsg = "Backend se connect nahi ho paya. localhost:8000 chal raha hai?";
      } else if (e.message?.includes("capture")) {
        userMsg = "Screenshot lene mein problem aayi. Tab active hai?";
      } else if (e.message?.includes("HTTP")) {
        userMsg = `Backend error: ${e.message}`;
      }

      await safeSendMessage(tabId, {
        action: "display_error",
        message: userMsg,
      });
    }
  })();

  return true; // ✅ Async response ke liye zaroori
});

// ─── Helper: Tab Capture ──────────────────────────────

function captureTab(windowId) {
  return new Promise((resolve, reject) => {
    try {
      chrome.tabs.captureVisibleTab(windowId, { format: "png" }, (dataUrl) => {
        if (chrome.runtime.lastError) {
          reject(new Error("capture: " + chrome.runtime.lastError.message));
        } else if (!dataUrl) {
          reject(new Error("capture: empty dataUrl returned"));
        } else {
          resolve(dataUrl);
        }
      });
    } catch (e) {
      reject(new Error("capture: " + e.message));
    }
  });
}

// ─── Helper: DataURL → Blob ───────────────────────────

async function dataUrlToBlob(dataUrl) {
  try {
    const res = await fetch(dataUrl);
    if (!res.ok) throw new Error("blob fetch failed");
    return await res.blob();
  } catch (e) {
    throw new Error("blob conversion failed: " + e.message);
  }
}

// ─── Helper: Crop Image using OffscreenCanvas ─────────

async function cropImage(dataUrl, rect) {
  try {
    // dataUrl ko blob mein convert karo
    const res = await fetch(dataUrl);
    const blob = await res.blob();

    // ImageBitmap banao
    const img = await createImageBitmap(blob);

    // DPR (device pixel ratio) ke hisaab se actual pixels calculate karo
    const dpr = rect.dpr || 1;
    const sx = rect.x * dpr;
    const sy = rect.y * dpr;
    const sw = rect.width * dpr;
    const sh = rect.height * dpr;

    // OffscreenCanvas par crop karo
    const canvas = new OffscreenCanvas(sw, sh);
    const ctx = canvas.getContext("2d");
    ctx.drawImage(img, sx, sy, sw, sh, 0, 0, sw, sh);

    // Canvas ko blob mein convert karo
    const croppedBlob = await canvas.convertToBlob({ type: "image/png" });

    // Blob ko dataUrl mein convert karo
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(new Error("Crop: FileReader failed"));
      reader.readAsDataURL(croppedBlob);
    });
  } catch (e) {
    console.warn("[CircleSearch] Crop failed, using full screenshot:", e.message);
    return dataUrl; // Crop fail hone par poora screenshot use karo
  }
}


async function callBackend(formData) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12000); // 12s timeout

  let response;
  try {
    response = await fetch(`${API_BASE}/predict`, {
      method: "POST",
      body: formData,
      signal: controller.signal,
    });
  } catch (e) {
    clearTimeout(timeout);
    if (e.name === "AbortError") {
      throw new Error("timeout: backend ne 12s mein respond nahi kiya");
    }
    throw new Error("fetch: " + e.message);
  }

  clearTimeout(timeout);

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  try {
    return await response.json();
  } catch (e) {
    throw new Error("JSON parse failed: backend ne invalid response diya");
  }
}