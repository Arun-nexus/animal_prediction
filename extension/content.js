(function () {
  if (window.__circleSearchInjected) return;
  window.__circleSearchInjected = true;

  // ─── Message Listener ────────────────────────────────
  chrome.runtime.onMessage.addListener((msg) => {
    if (msg.action === "open_overlay") startSelection();
    if (msg.action === "display_result") showResult(msg.data);
    if (msg.action === "display_error") showToast(msg.message, true);
    if (msg.action === "show_loading") showLoading();
  });

  // ─── Rectangle Selection ─────────────────────────────
  function startSelection() {
    if (document.getElementById("cs-overlay")) return;

    document.body.style.overflow = "hidden";

    const overlay = document.createElement("div");
    overlay.id = "cs-overlay";
    overlay.style.cssText = `
      position:fixed; top:0; left:0;
      width:100vw; height:100vh;
      background:rgba(0,0,0,0.5);
      z-index:2147483647;
      cursor:crosshair;
      user-select:none;
    `;
    document.body.appendChild(overlay);

    const hint = document.createElement("div");
    hint.style.cssText = `
      position:fixed; top:16px; left:50%;
      transform:translateX(-50%);
      background:rgba(0,0,0,0.75); color:#fff;
      font-family:sans-serif; font-size:13px;
      padding:8px 18px; border-radius:20px;
      z-index:2147483648; pointer-events:none;
    `;
    hint.innerText = "Drag karo area select karne ke liye  •  ESC = cancel";
    document.body.appendChild(hint);

    const box = document.createElement("div");
    box.style.cssText = `
      position:fixed;
      border:2px solid #4A90E2;
      background:rgba(74,144,226,0.08);
      border-radius:2px;
      pointer-events:none;
      display:none;
      z-index:2147483648;
    `;
    document.body.appendChild(box);

    let startX, startY, isDragging = false;

    function cleanup() {
      overlay.remove();
      box.remove();
      hint.remove();
      document.body.style.overflow = "";
      document.removeEventListener("keydown", onKeyDown);
    }

    overlay.addEventListener("mousedown", (e) => {
      e.preventDefault();
      startX = e.clientX;
      startY = e.clientY;
      isDragging = true;
      box.style.display = "block";
      box.style.left = startX + "px";
      box.style.top  = startY + "px";
      box.style.width = "0px";
      box.style.height = "0px";
    });

    overlay.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      box.style.left   = Math.min(e.clientX, startX) + "px";
      box.style.top    = Math.min(e.clientY, startY) + "px";
      box.style.width  = Math.abs(e.clientX - startX) + "px";
      box.style.height = Math.abs(e.clientY - startY) + "px";
    });

    overlay.addEventListener("mouseup", (e) => {
      if (!isDragging) return;
      isDragging = false;

      const x = Math.min(e.clientX, startX);
      const y = Math.min(e.clientY, startY);
      const w = Math.abs(e.clientX - startX);
      const h = Math.abs(e.clientY - startY);

      if (w < 10 || h < 10) { cleanup(); return; }

      cleanup();

      chrome.runtime.sendMessage({
        action: "capture_screen",
        cropRect: {
          x: Math.round(x),
          y: Math.round(y),
          width: Math.round(w),
          height: Math.round(h),
          dpr: window.devicePixelRatio || 1,
        },
      });

      showLoading();
    });

    function onKeyDown(e) {
      if (e.key === "Escape") cleanup();
    }
    document.addEventListener("keydown", onKeyDown);
  }

  // ─── Loading ──────────────────────────────────────────
  function showLoading() {
    removeById("cs-result");
    removeById("cs-loading");

    if (!document.getElementById("cs-style")) {
      const style = document.createElement("style");
      style.id = "cs-style";
      style.textContent = `@keyframes cs-spin { to { transform:rotate(360deg); } }`;
      document.head.appendChild(style);
    }

    const el = document.createElement("div");
    el.id = "cs-loading";
    el.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      background:#111; color:#fff;
      font-family:sans-serif; font-size:14px;
      padding:14px 20px; border-radius:12px;
      z-index:2147483647;
      display:flex; align-items:center; gap:10px;
      box-shadow:0 8px 24px rgba(0,0,0,0.3);
    `;
    el.innerHTML = `
      <div style="width:16px;height:16px;border:2px solid rgba(255,255,255,0.3);
        border-top-color:#fff;border-radius:50%;
        animation:cs-spin 0.8s linear infinite;"></div>
      Analyzing...
    `;
    document.body.appendChild(el);
  }

  // ─── Result Panel ─────────────────────────────────────
  function showResult(data) {
    removeById("cs-loading");
    removeById("cs-result");
    removeById("cs-chat");

    const confidence = data.confidence != null
      ? (data.confidence * 100).toFixed(1) + "%"
      : "N/A";

    const confColor =
      data.confidence >= 0.8 ? "#22c55e" :
      data.confidence >= 0.5 ? "#f59e0b" : "#ef4444";

    const panel = document.createElement("div");
    panel.id = "cs-result";
    panel.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      width:290px; background:#fff;
      border-radius:14px;
      box-shadow:0 8px 32px rgba(0,0,0,0.18);
      z-index:2147483647;
      font-family:sans-serif;
      overflow:hidden;
      border:1px solid #e5e5e5;
    `;

    panel.innerHTML = `
      <div style="background:#111;color:#fff;padding:14px 16px;
          display:flex;justify-content:space-between;align-items:center;">
        <span style="font-weight:600;font-size:14px;">🔍 Circle Search AI</span>
        <span id="cs-close" style="cursor:pointer;font-size:20px;opacity:0.7;line-height:1;">×</span>
      </div>
      <div style="padding:16px;">

        <div style="font-size:11px;color:#888;margin-bottom:3px;
            text-transform:uppercase;letter-spacing:0.5px;">Detected</div>
        <div style="font-size:20px;font-weight:700;color:#111;
            margin-bottom:12px;">${data.class || "Unknown"}</div>

        <div style="display:flex;justify-content:space-between;align-items:center;
            background:#f5f5f5;border-radius:8px;padding:10px 14px;margin-bottom:12px;">
          <span style="font-size:13px;color:#555;">Confidence</span>
          <span style="font-size:15px;font-weight:700;color:${confColor};">${confidence}</span>
        </div>

        ${data.info ? `
        <div style="font-size:12px;color:#444;line-height:1.6;
            background:#fafafa;border-radius:8px;padding:10px 12px;
            margin-bottom:12px;border:1px solid #eee;
            max-height:80px;overflow-y:auto;">
          ${data.info}
        </div>` : ""}

        <button id="cs-ask-grok" style="
          width:100%;padding:11px;
          background:#111;color:#fff;border:none;
          border-radius:8px;cursor:pointer;font-size:13px;
          font-weight:600;letter-spacing:0.3px;
          display:flex;align-items:center;justify-content:center;gap:8px;">
          <span>🤖</span> Ask Grok AI
        </button>
      </div>
    `;

    document.body.appendChild(panel);

    document.getElementById("cs-close").onclick = () => {
      removeById("cs-result");
      removeById("cs-chat");
    };

    document.getElementById("cs-ask-grok").onclick = () => {
      // Panel ko left shift karo chat ke liye jagah banane ke liye
      panel.style.right = "430px";
      openGrokChat(data.class);
    };
  }

  // ─── Grok Chat ────────────────────────────────────────
  function openGrokChat(detectedClass) {
    if (document.getElementById("cs-chat")) return;

    const chat = document.createElement("div");
    chat.id = "cs-chat";
    chat.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      width:370px; height:490px;
      background:#fff; border-radius:14px;
      box-shadow:0 8px 32px rgba(0,0,0,0.18);
      z-index:2147483647;
      display:flex; flex-direction:column;
      border:1px solid #e5e5e5;
      overflow:hidden;
      font-family:sans-serif;
    `;

    chat.innerHTML = `
      <div style="background:#111;color:#fff;padding:14px 16px;
          display:flex;justify-content:space-between;align-items:center;
          flex-shrink:0;">
        <span style="font-weight:600;font-size:14px;">🤖 Grok AI</span>
        <span id="cs-chat-close" style="cursor:pointer;font-size:20px;
            opacity:0.7;line-height:1;">×</span>
      </div>

      <div id="cs-msg-box" style="
        flex:1;overflow-y:auto;padding:14px;
        display:flex;flex-direction:column;gap:10px;
        scroll-behavior:smooth;
      "></div>

      <div id="cs-ws-status" style="
        text-align:center;font-size:11px;color:#aaa;
        padding:4px 0;flex-shrink:0;
      ">Connecting...</div>

      <div style="padding:10px;border-top:1px solid #eee;
          display:flex;gap:8px;flex-shrink:0;">
        <input id="cs-input" style="
          flex:1;padding:9px 12px;
          border:1px solid #ddd;border-radius:8px;
          outline:none;font-size:13px;
          font-family:sans-serif;
        " placeholder="Kuch bhi poochho...">
        <button id="cs-send" style="
          padding:9px 14px;background:#111;color:#fff;
          border:none;border-radius:8px;cursor:pointer;
          font-size:15px;
        ">➤</button>
      </div>
    `;

    document.body.appendChild(chat);

    // Detected animal ka naam pre-fill karo
    if (detectedClass) {
      document.getElementById("cs-input").value = `Tell me about ${detectedClass}`;
    }

    const msgBox    = document.getElementById("cs-msg-box");
    const statusEl  = document.getElementById("cs-ws-status");
    const inputEl   = document.getElementById("cs-input");
    const sendBtn   = document.getElementById("cs-send");

    sendBtn.disabled = true;
    let currentBubble = null;
    let ws;

    // ── WebSocket connect ──
    function connect() {
      try {
        ws = new WebSocket("ws://localhost:8000/query/123");
      } catch (e) {
        statusEl.textContent = "❌ Connection failed";
        return;
      }

      ws.onopen = () => {
        statusEl.textContent = "🟢 Connected";
        sendBtn.disabled = false;
      };

      ws.onclose = () => {
        statusEl.textContent = "🔴 Disconnected";
        sendBtn.disabled = true;
      };

      ws.onerror = () => {
        statusEl.textContent = "❌ WebSocket error";
        sendBtn.disabled = true;
      };

      ws.onmessage = (e) => {
        const text = e.data;

        // [END] = response complete
        if (text === "[END]") {
          currentBubble = null;
          return;
        }

        // [error] = backend error
        if (text.startsWith("[error]")) {
          addBubble(text.replace("[error]", "⚠️").trim(), "error");
          currentBubble = null;
          return;
        }

        // Streaming text — same bubble mein append karo
        if (!currentBubble) {
          currentBubble = document.createElement("div");
          currentBubble.style.cssText = `
            background:#f1f1f1;
            padding:10px 12px;
            border-radius:10px 10px 10px 2px;
            align-self:flex-start;
            max-width:88%;
            font-size:13px;
            line-height:1.6;
            color:#111;
          `;
          msgBox.appendChild(currentBubble);
        }

        currentBubble.textContent += text;
        msgBox.scrollTop = msgBox.scrollHeight;
      };
    }

    connect();

    // ── Send message ──
    function sendMessage() {
      const val = inputEl.value.trim();
      if (!val) return;
      if (!ws || ws.readyState !== WebSocket.OPEN) {
        statusEl.textContent = "❌ Not connected";
        return;
      }

      // User bubble
      addBubble(val, "user");
      ws.send(val);
      inputEl.value = "";
      currentBubble = null;
    }

    function addBubble(text, type) {
      const el = document.createElement("div");
      if (type === "user") {
        el.style.cssText = `
          background:#111; color:#fff;
          padding:10px 12px;
          border-radius:10px 10px 2px 10px;
          align-self:flex-end;
          max-width:88%;
          font-size:13px;
          line-height:1.6;
        `;
      } else {
        el.style.cssText = `
          background:#fff3cd; color:#856404;
          padding:10px 12px;
          border-radius:10px;
          align-self:flex-start;
          max-width:88%;
          font-size:13px;
        `;
      }
      el.textContent = text;
      msgBox.appendChild(el);
      msgBox.scrollTop = msgBox.scrollHeight;
    }

    sendBtn.onclick = sendMessage;
    inputEl.onkeydown = (e) => { if (e.key === "Enter") sendMessage(); };

    document.getElementById("cs-chat-close").onclick = () => {
      if (ws) ws.close();
      chat.remove();
      // Result panel wapas right mein
      const panel = document.getElementById("cs-result");
      if (panel) panel.style.right = "24px";
    };
  }

  // ─── Toast ────────────────────────────────────────────
  function showToast(message, isError = false) {
    removeById("cs-loading");
    removeById("cs-toast");

    const toast = document.createElement("div");
    toast.id = "cs-toast";
    toast.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      background:${isError ? "#ef4444" : "#22c55e"};
      color:#fff; font-family:sans-serif; font-size:13px;
      padding:12px 18px; border-radius:10px;
      z-index:2147483647;
      box-shadow:0 4px 16px rgba(0,0,0,0.2);
      max-width:280px;
    `;
    toast.innerText = (isError ? "❌ " : "✅ ") + message;
    document.body.appendChild(toast);
    setTimeout(() => removeById("cs-toast"), 4000);
  }

  // ─── Utility ──────────────────────────────────────────
  function removeById(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

})();(function () {
  if (window.__circleSearchInjected) return;
  window.__circleSearchInjected = true;

  // ─── Message Listener ────────────────────────────────
  chrome.runtime.onMessage.addListener((msg) => {
    if (msg.action === "open_overlay") startSelection();
    if (msg.action === "display_result") showResult(msg.data);
    if (msg.action === "display_error") showToast(msg.message, true);
    if (msg.action === "show_loading") showLoading();
  });

  // ─── Rectangle Selection ─────────────────────────────
  function startSelection() {
    if (document.getElementById("cs-overlay")) return;

    document.body.style.overflow = "hidden";

    const overlay = document.createElement("div");
    overlay.id = "cs-overlay";
    overlay.style.cssText = `
      position:fixed; top:0; left:0;
      width:100vw; height:100vh;
      background:rgba(0,0,0,0.5);
      z-index:2147483647;
      cursor:crosshair;
      user-select:none;
    `;
    document.body.appendChild(overlay);

    const hint = document.createElement("div");
    hint.style.cssText = `
      position:fixed; top:16px; left:50%;
      transform:translateX(-50%);
      background:rgba(0,0,0,0.75); color:#fff;
      font-family:sans-serif; font-size:13px;
      padding:8px 18px; border-radius:20px;
      z-index:2147483648; pointer-events:none;
    `;
    hint.innerText = "Drag karo area select karne ke liye  •  ESC = cancel";
    document.body.appendChild(hint);

    const box = document.createElement("div");
    box.style.cssText = `
      position:fixed;
      border:2px solid #4A90E2;
      background:rgba(74,144,226,0.08);
      border-radius:2px;
      pointer-events:none;
      display:none;
      z-index:2147483648;
    `;
    document.body.appendChild(box);

    let startX, startY, isDragging = false;

    function cleanup() {
      overlay.remove();
      box.remove();
      hint.remove();
      document.body.style.overflow = "";
      document.removeEventListener("keydown", onKeyDown);
    }

    overlay.addEventListener("mousedown", (e) => {
      e.preventDefault();
      startX = e.clientX;
      startY = e.clientY;
      isDragging = true;
      box.style.display = "block";
      box.style.left = startX + "px";
      box.style.top  = startY + "px";
      box.style.width = "0px";
      box.style.height = "0px";
    });

    overlay.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      box.style.left   = Math.min(e.clientX, startX) + "px";
      box.style.top    = Math.min(e.clientY, startY) + "px";
      box.style.width  = Math.abs(e.clientX - startX) + "px";
      box.style.height = Math.abs(e.clientY - startY) + "px";
    });

    overlay.addEventListener("mouseup", (e) => {
      if (!isDragging) return;
      isDragging = false;

      const x = Math.min(e.clientX, startX);
      const y = Math.min(e.clientY, startY);
      const w = Math.abs(e.clientX - startX);
      const h = Math.abs(e.clientY - startY);

      if (w < 10 || h < 10) { cleanup(); return; }

      cleanup();

      chrome.runtime.sendMessage({
        action: "capture_screen",
        cropRect: {
          x: Math.round(x),
          y: Math.round(y),
          width: Math.round(w),
          height: Math.round(h),
          dpr: window.devicePixelRatio || 1,
        },
      });

      showLoading();
    });

    function onKeyDown(e) {
      if (e.key === "Escape") cleanup();
    }
    document.addEventListener("keydown", onKeyDown);
  }

  // ─── Loading ──────────────────────────────────────────
  function showLoading() {
    removeById("cs-result");
    removeById("cs-loading");

    if (!document.getElementById("cs-style")) {
      const style = document.createElement("style");
      style.id = "cs-style";
      style.textContent = `@keyframes cs-spin { to { transform:rotate(360deg); } }`;
      document.head.appendChild(style);
    }

    const el = document.createElement("div");
    el.id = "cs-loading";
    el.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      background:#111; color:#fff;
      font-family:sans-serif; font-size:14px;
      padding:14px 20px; border-radius:12px;
      z-index:2147483647;
      display:flex; align-items:center; gap:10px;
      box-shadow:0 8px 24px rgba(0,0,0,0.3);
    `;
    el.innerHTML = `
      <div style="width:16px;height:16px;border:2px solid rgba(255,255,255,0.3);
        border-top-color:#fff;border-radius:50%;
        animation:cs-spin 0.8s linear infinite;"></div>
      Analyzing...
    `;
    document.body.appendChild(el);
  }

  // ─── Result Panel ─────────────────────────────────────
  function showResult(data) {
    removeById("cs-loading");
    removeById("cs-result");
    removeById("cs-chat");

    const confidence = data.confidence != null
      ? (data.confidence * 100).toFixed(1) + "%"
      : "N/A";

    const confColor =
      data.confidence >= 0.8 ? "#22c55e" :
      data.confidence >= 0.5 ? "#f59e0b" : "#ef4444";

    const panel = document.createElement("div");
    panel.id = "cs-result";
    panel.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      width:290px; background:#fff;
      border-radius:14px;
      box-shadow:0 8px 32px rgba(0,0,0,0.18);
      z-index:2147483647;
      font-family:sans-serif;
      overflow:hidden;
      border:1px solid #e5e5e5;
    `;

    panel.innerHTML = `
      <div style="background:#111;color:#fff;padding:14px 16px;
          display:flex;justify-content:space-between;align-items:center;">
        <span style="font-weight:600;font-size:14px;">🔍 Circle Search AI</span>
        <span id="cs-close" style="cursor:pointer;font-size:20px;opacity:0.7;line-height:1;">×</span>
      </div>
      <div style="padding:16px;">

        <div style="font-size:11px;color:#888;margin-bottom:3px;
            text-transform:uppercase;letter-spacing:0.5px;">Detected</div>
        <div style="font-size:20px;font-weight:700;color:#111;
            margin-bottom:12px;">${data.class || "Unknown"}</div>

        <div style="display:flex;justify-content:space-between;align-items:center;
            background:#f5f5f5;border-radius:8px;padding:10px 14px;margin-bottom:12px;">
          <span style="font-size:13px;color:#555;">Confidence</span>
          <span style="font-size:15px;font-weight:700;color:${confColor};">${confidence}</span>
        </div>

        ${data.info ? `
        <div style="font-size:12px;color:#444;line-height:1.6;
            background:#fafafa;border-radius:8px;padding:10px 12px;
            margin-bottom:12px;border:1px solid #eee;
            max-height:80px;overflow-y:auto;">
          ${data.info}
        </div>` : ""}

        <button id="cs-ask-grok" style="
          width:100%;padding:11px;
          background:#111;color:#fff;border:none;
          border-radius:8px;cursor:pointer;font-size:13px;
          font-weight:600;letter-spacing:0.3px;
          display:flex;align-items:center;justify-content:center;gap:8px;">
          <span>🤖</span> Ask Grok AI
        </button>
      </div>
    `;

    document.body.appendChild(panel);

    document.getElementById("cs-close").onclick = () => {
      removeById("cs-result");
      removeById("cs-chat");
    };

    document.getElementById("cs-ask-grok").onclick = () => {
      // Panel ko left shift karo chat ke liye jagah banane ke liye
      panel.style.right = "430px";
      openGrokChat(data.class);
    };
  }

  // ─── Grok Chat ────────────────────────────────────────
  function openGrokChat(detectedClass) {
    if (document.getElementById("cs-chat")) return;

    const chat = document.createElement("div");
    chat.id = "cs-chat";
    chat.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      width:370px; height:490px;
      background:#fff; border-radius:14px;
      box-shadow:0 8px 32px rgba(0,0,0,0.18);
      z-index:2147483647;
      display:flex; flex-direction:column;
      border:1px solid #e5e5e5;
      overflow:hidden;
      font-family:sans-serif;
    `;

    chat.innerHTML = `
      <div style="background:#111;color:#fff;padding:14px 16px;
          display:flex;justify-content:space-between;align-items:center;
          flex-shrink:0;">
        <span style="font-weight:600;font-size:14px;">🤖 Grok AI</span>
        <span id="cs-chat-close" style="cursor:pointer;font-size:20px;
            opacity:0.7;line-height:1;">×</span>
      </div>

      <div id="cs-msg-box" style="
        flex:1;overflow-y:auto;padding:14px;
        display:flex;flex-direction:column;gap:10px;
        scroll-behavior:smooth;
      "></div>

      <div id="cs-ws-status" style="
        text-align:center;font-size:11px;color:#aaa;
        padding:4px 0;flex-shrink:0;
      ">Connecting...</div>

      <div style="padding:10px;border-top:1px solid #eee;
          display:flex;gap:8px;flex-shrink:0;">
        <input id="cs-input" style="
          flex:1;padding:9px 12px;
          border:1px solid #ddd;border-radius:8px;
          outline:none;font-size:13px;
          font-family:sans-serif;
        " placeholder="Kuch bhi poochho...">
        <button id="cs-send" style="
          padding:9px 14px;background:#111;color:#fff;
          border:none;border-radius:8px;cursor:pointer;
          font-size:15px;
        ">➤</button>
      </div>
    `;

    document.body.appendChild(chat);

    // Detected animal ka naam pre-fill karo
    if (detectedClass) {
      document.getElementById("cs-input").value = `Tell me about ${detectedClass}`;
    }

    const msgBox    = document.getElementById("cs-msg-box");
    const statusEl  = document.getElementById("cs-ws-status");
    const inputEl   = document.getElementById("cs-input");
    const sendBtn   = document.getElementById("cs-send");

    sendBtn.disabled = true;
    let currentBubble = null;
    let ws;

    // ── WebSocket connect ──
    function connect() {
      try {
        ws = new WebSocket("ws://localhost:8000/query/123");
      } catch (e) {
        statusEl.textContent = "❌ Connection failed";
        return;
      }

      ws.onopen = () => {
        statusEl.textContent = "🟢 Connected";
        sendBtn.disabled = false;
      };

      ws.onclose = () => {
        statusEl.textContent = "🔴 Disconnected";
        sendBtn.disabled = true;
      };

      ws.onerror = () => {
        statusEl.textContent = "❌ WebSocket error";
        sendBtn.disabled = true;
      };

      ws.onmessage = (e) => {
        const text = e.data;

        // [END] = response complete
        if (text === "[END]") {
          currentBubble = null;
          return;
        }

        // [error] = backend error
        if (text.startsWith("[error]")) {
          addBubble(text.replace("[error]", "⚠️").trim(), "error");
          currentBubble = null;
          return;
        }

        // Streaming text — same bubble mein append karo
        if (!currentBubble) {
          currentBubble = document.createElement("div");
          currentBubble.style.cssText = `
            background:#f1f1f1;
            padding:10px 12px;
            border-radius:10px 10px 10px 2px;
            align-self:flex-start;
            max-width:88%;
            font-size:13px;
            line-height:1.6;
            color:#111;
          `;
          msgBox.appendChild(currentBubble);
        }

        currentBubble.textContent += text;
        msgBox.scrollTop = msgBox.scrollHeight;
      };
    }

    connect();

    // ── Send message ──
    function sendMessage() {
      const val = inputEl.value.trim();
      if (!val) return;
      if (!ws || ws.readyState !== WebSocket.OPEN) {
        statusEl.textContent = "❌ Not connected";
        return;
      }

      // User bubble
      addBubble(val, "user");
      ws.send(val);
      inputEl.value = "";
      currentBubble = null;
    }

    function addBubble(text, type) {
      const el = document.createElement("div");
      if (type === "user") {
        el.style.cssText = `
          background:#111; color:#fff;
          padding:10px 12px;
          border-radius:10px 10px 2px 10px;
          align-self:flex-end;
          max-width:88%;
          font-size:13px;
          line-height:1.6;
        `;
      } else {
        el.style.cssText = `
          background:#fff3cd; color:#856404;
          padding:10px 12px;
          border-radius:10px;
          align-self:flex-start;
          max-width:88%;
          font-size:13px;
        `;
      }
      el.textContent = text;
      msgBox.appendChild(el);
      msgBox.scrollTop = msgBox.scrollHeight;
    }

    sendBtn.onclick = sendMessage;
    inputEl.onkeydown = (e) => { if (e.key === "Enter") sendMessage(); };

    document.getElementById("cs-chat-close").onclick = () => {
      if (ws) ws.close();
      chat.remove();
      // Result panel wapas right mein
      const panel = document.getElementById("cs-result");
      if (panel) panel.style.right = "24px";
    };
  }

  // ─── Toast ────────────────────────────────────────────
  function showToast(message, isError = false) {
    removeById("cs-loading");
    removeById("cs-toast");

    const toast = document.createElement("div");
    toast.id = "cs-toast";
    toast.style.cssText = `
      position:fixed; bottom:24px; right:24px;
      background:${isError ? "#ef4444" : "#22c55e"};
      color:#fff; font-family:sans-serif; font-size:13px;
      padding:12px 18px; border-radius:10px;
      z-index:2147483647;
      box-shadow:0 4px 16px rgba(0,0,0,0.2);
      max-width:280px;
    `;
    toast.innerText = (isError ? "❌ " : "✅ ") + message;
    document.body.appendChild(toast);
    setTimeout(() => removeById("cs-toast"), 4000);
  }

  // ─── Utility ──────────────────────────────────────────
  function removeById(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

})();