const gotTo = (url) => window.location.replace(url);

document.getElementById("helloWorldButton").addEventListener("click", () => { eel.hello_world() }, false);
document.getElementById("goToScan").addEventListener("click", () => { gotTo('./pages/scan.html') }, false);
document.getElementById("goToHome").addEventListener("click", () => { gotTo('./index.html') }, false);

eel.expose(prompt_alerts);

function prompt_alerts(description) {
    alert(description);
}