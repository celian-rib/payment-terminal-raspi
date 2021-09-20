document.getElementById("button-name").addEventListener("click", ()=>{eel.get_random_name()}, false);
document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);
document.getElementById("button-kill").addEventListener("click", ()=>{eel.kill()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

eel.expose(printalert);
function printalert(a) {
  alert(a);
}