(function() {
    if (window.hasRun) return;
    window.hasRun = true;

    chrome.runtime.onMessage.addListener((msg) => {
        if (msg.action === "open_overlay") startSelection();
        if (msg.action === "display_result") showResultUI(msg.data);
    });

    function startSelection() {
        if (document.getElementById("circle-overlay")) return;
        const overlay = document.createElement("div");
        overlay.id = "circle-overlay";
        overlay.style.cssText = "position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.4);z-index:2147483647;cursor:crosshair;";
        document.body.appendChild(overlay);

        let startX, startY, box = document.createElement("div");
        box.style.cssText = "position:absolute;border:2px solid #fff;box-shadow:0 0 0 9999px rgba(0,0,0,0.5);pointer-events:none;";
        overlay.appendChild(box);

        overlay.onmousedown = (e) => { startX = e.clientX; startY = e.clientY; };
        overlay.onmousemove = (e) => {
            if (e.buttons !== 1) return;
            box.style.width = Math.abs(e.clientX - startX) + "px";
            box.style.height = Math.abs(e.clientY - startY) + "px";
            box.style.left = Math.min(e.clientX, startX) + "px";
            box.style.top = Math.min(e.clientY, startY) + "px";
        };
        overlay.onmouseup = () => {
            chrome.runtime.sendMessage({ action: "capture_screen" });
            overlay.remove();
        };
    }

    function showResultUI(data) {
        let panel = document.getElementById("ai-panel-root");
        if (panel) panel.remove();

        panel = document.createElement("div");
        panel.id = "ai-panel-root";
        panel.style.cssText = "position:fixed;bottom:20px;right:20px;width:300px;background:white;padding:20px;border-radius:15px;box-shadow:0 10px 30px rgba(0,0,0,0.5);z-index:2147483647;color:black;font-family:sans-serif;border:1px solid #ddd;";
        
        panel.innerHTML = `
            <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
                <b style="font-size:16px;">AI Result</b>
                <span id="close-x" style="cursor:pointer;font-weight:bold;">&times;</span>
            </div>
            <div style="background:#f9f9f9;padding:10px;border-radius:8px;">
                <b>Detected:</b> ${data.class}<br>
                <b>Match:</b> ${(data.confidence * 100).toFixed(1)}%
            </div>
            <button id="ask-grok" style="width:100%;margin-top:15px;padding:10px;background:black;color:white;border-radius:8px;cursor:pointer;border:none;">Ask Grok AI</button>
        `;
        document.body.appendChild(panel);

        document.getElementById("close-x").onclick = () => panel.remove();
        document.getElementById("ask-grok").onclick = () => {
            panel.style.right = "430px";
            openGrokChat();
        };
    }

    function openGrokChat() {
        if (document.getElementById("grok-chat")) return;
        const chat = document.createElement("div");
        chat.id = "grok-chat";
        chat.style.cssText = "position:fixed;bottom:20px;right:20px;width:380px;height:500px;background:white;border-radius:15px;box-shadow:0 10px 30px rgba(0,0,0,0.5);z-index:2147483647;display:flex;flex-direction:column;border:1px solid #ddd;overflow:hidden;color:black;font-family:sans-serif;";
        
        chat.innerHTML = `
            <div style="background:black;color:white;padding:15px;display:flex;justify-content:space-between;">
                <b>Grok AI</b> <span id="close-g" style="cursor:pointer;">&times;</span>
            </div>
            <div id="m-box" style="flex:1;overflow-y:auto;padding:15px;display:flex;flex-direction:column;gap:10px;"></div>
            <div style="padding:10px;border-top:1px solid #eee;display:flex;">
                <input id="g-in" style="flex:1;padding:8px;border:1px solid #ddd;border-radius:5px;" placeholder="Ask...">
                <button id="g-send" style="margin-left:5px;padding:8px;background:blue;color:white;border:none;border-radius:5px;">Send</button>
            </div>
        `;
        document.body.appendChild(chat);

        const ws = new WebSocket("ws://localhost:8000/query/123");
        let currentDiv = null;

        ws.onmessage = (e) => {
            if (!currentDiv) {
                currentDiv = document.createElement("div");
                currentDiv.style.cssText = "background:#f1f1f1;padding:8px;border-radius:8px;align-self:flex-start;max-width:80%;";
                currentDiv.innerHTML = "<b>Grok:</b> ";
                document.getElementById("m-box").appendChild(currentDiv);
            }
            currentDiv.innerHTML += e.data;
            document.getElementById("m-box").scrollTop = document.getElementById("m-box").scrollHeight;
        };

        document.getElementById("g-send").onclick = () => {
            const val = document.getElementById("g-in").value;
            if (val && ws.readyState === 1) {
                ws.send(val);
                const uMsg = document.createElement("div");
                uMsg.style.cssText = "background:blue;color:white;padding:8px;border-radius:8px;align-self:flex-end;max-width:80%;";
                uMsg.innerText = val;
                document.getElementById("m-box").appendChild(uMsg);
                document.getElementById("g-in").value = "";
                currentDiv = null;
            }
        };

        document.getElementById("close-g").onclick = () => { chat.remove(); document.getElementById("ai-panel-root").style.right = "20px"; };
    }
})();