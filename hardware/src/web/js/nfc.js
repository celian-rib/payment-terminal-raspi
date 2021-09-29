let price = "loading ...";

const base = "En attente de la carte";
const animation_tick = 200;

const delay = async (duration) => new Promise((resolve) => setTimeout(() => resolve(), duration));

function textAnimation() {
    const text = document.getElementById("textWriter");
    const anim = async () => {
        text.innerHTML = base
        await delay(animation_tick)
        text.innerHTML = base + "."
        await delay(animation_tick)
        text.innerHTML = base + ".."
        await delay(animation_tick)
        text.innerHTML = base + "..."
        await delay(animation_tick)
        anim()
    }
    anim()
}

eel.expose(scan_complete)
function scan_complete(money, userID) {
    goToWithParam("goToValidTransac", "?money=" + money + "&userID=" + userID);
}

eel.expose(scan_cancel)
function scan_cancel(money, userID, reason) {
    goToWithParam("goToUnvalidTransac", "?money=" + money + "&userID=" + userID + "&reason=" + reason);
}

window.onload = function() {
    // Retreive price from url
    const urlData = parseURLParams(window.location.href);
    price = Object.keys(urlData)[0];
    priceText.innerHTML = getPriceString(price);

    // Start transaction on python side
    eel.await_card_scan(price);

    textAnimation()
}