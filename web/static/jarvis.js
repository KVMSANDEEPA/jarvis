function appendMessage(sender, message){
    const chatBox=document.getElementById("chat-box");
    const msg=document.createElement("div");
    msg.className=sender.toLowerCase()+"-msg";
    msg.innerHTML=`<span>${sender}:</span> ${message}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop=chatBox.scrollHeight;
}

async function sendMessage(){
    const input=document.getElementById("user-input");
    const message=input.value.trim(); if(!message) return; appendMessage("You",message); input.value="";
    const res=await fetch("/send",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message})});
    const data=await res.json(); appendMessage("Jarvis",data.reply); speak(data.reply);
}

function speak(text){const synth=window.speechSynthesis; const utter=new SpeechSynthesisUtterance(text); synth.speak(utter);}

document.getElementById("send-btn").onclick=sendMessage;
document.getElementById("user-input").addEventListener("keypress",e=>{if(e.key==="Enter")sendMessage();});

document.getElementById("voice-btn").onclick=()=>{
    const recognition=new(window.SpeechRecognition||window.webkitSpeechRecognition)();
    recognition.lang="en-US"; recognition.start();
    recognition.onresult=async e=>{
        const transcript=e.results[0][0].transcript;
        appendMessage("You",transcript);
        const res=await fetch("/send",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:transcript})});
        const data=await res.json(); appendMessage("Jarvis",data.reply); speak(data.reply);
    }
}

function sendShortcut(cmd){appendMessage("You",cmd); fetch("/send",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:cmd})}).then(res=>res.json()).then(data=>{appendMessage("Jarvis",data.reply); speak(data.reply);});}

// Holographic animation
const canvas=document.getElementById("holo-bg"); const ctx=canvas.getContext("2d"); canvas.width=window.innerWidth; canvas.height=window.innerHeight;
let lines=[]; for(let i=0;i<50;i++){lines.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,dx:(Math.random()-0.5)*1.5,dy:(Math.random()-0.5)*1.5,length:20+Math.random()*30});}
function animate(){ctx.clearRect(0,0,canvas.width,canvas.height); lines.forEach(l=>{ctx.beginPath(); ctx.strokeStyle="rgba(0,234,255,0.7)"; ctx.moveTo(l.x,l.y); ctx.lineTo(l.x+l.length,l.y+l.length); ctx.stroke(); l.x+=l.dx; l.y+=l.dy; if(l.x>canvas.width||l.x<0) l.dx*=-1; if(l.y>canvas.height||l.y<0) l.dy*=-1;}); requestAnimationFrame(animate);}
animate();
