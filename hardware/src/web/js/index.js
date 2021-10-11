window.onload = async function () {
    const image = window.navigator.onLine ? "img/wifion.png" : "img/wifioff.png";
    document.getElementById("connectionStatus").src = image;
}
