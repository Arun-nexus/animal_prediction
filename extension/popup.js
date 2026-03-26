let ws;

document.getElementById("start").onclick = () => {

    chrome.tabs.query({active:true,currentWindow:true}, (tabs)=>{

        chrome.tabs.sendMessage(tabs[0].id,{
            type:"start_capture"
        })

    })

}

chrome.storage.local.get("prediction",(data)=>{

    if(data.prediction){

        document.getElementById("result").innerText =
        data.prediction.class + " (" + data.prediction.confidence + ")"

        document.getElementById("query").style.display="block"

    }

})

document.getElementById("query").onclick=()=>{

    ws = new WebSocket("ws://localhost:8000/query/123")

    document.getElementById("msg").style.display="block"
    document.getElementById("send").style.display="block"

    ws.onmessage=(event)=>{
        document.getElementById("chat").innerHTML += event.data
    }

}

document.getElementById("send").onclick=()=>{

    const msg=document.getElementById("msg").value
    ws.send(msg)

}