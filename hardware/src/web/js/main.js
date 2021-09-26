const gotTo = (url) => window.location.replace(url);

if (document.getElementById("helloWorldButton"))
    document.getElementById("helloWorldButton").addEventListener("click", () => { eel.hello_world() }, false);

if (document.getElementById("goToScan"))
    document.getElementById("goToScan").addEventListener("click", () => { gotTo('./pages/scan.html') }, false);

if (document.getElementById("goToHome"))
    document.getElementById("goToHome").addEventListener("click", () => { gotTo('../index.html') }, false);


eel.expose(prompt_alerts);

function prompt_alerts(description) {
    alert(description);
}