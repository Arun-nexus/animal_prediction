let startX,startY

const overlay=document.createElement("div")
overlay.style.position="fixed"
overlay.style.top="0"
overlay.style.left="0"
overlay.style.width="100%"
overlay.style.height="100%"
overlay.style.background="rgba(0,0,0,0.4)"
overlay.style.zIndex="999999"

document.body.appendChild(overlay)

const box=document.createElement("div")
box.style.position="absolute"
box.style.border="2px solid red"
overlay.appendChild(box)

overlay.addEventListener("mousedown",(e)=>{

    startX=e.clientX
    startY=e.clientY

})

overlay.addEventListener("mousemove",(e)=>{

    const w=e.clientX-startX
    const h=e.clientY-startY

    box.style.left=startX+"px"
    box.style.top=startY+"px"
    box.style.width=w+"px"
    box.style.height=h+"px"

})

overlay.addEventListener("mouseup",(e)=>{

    chrome.runtime.sendMessage({
        type:"capture"
    })

    overlay.remove()

})