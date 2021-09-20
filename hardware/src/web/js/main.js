const gotTo = (url) => window.location.replace(url);

document.getElementById("hello-world-button").addEventListener("click", ()=>{eel.hello_world()}, false);
document.getElementById("go-to-scan").addEventListener("click", ()=>{gotTo('./pages/scan.html')}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}