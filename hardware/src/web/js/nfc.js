let price = "loading ...";

const base = "En attente de la carte";
const delay = 200;

window.onload = function() {

    console.log(window.location.href)
    const urlData = parseURLParams(window.location.href);
    price = Object.keys(urlData)[0];
    priceText.innerHTML = getPriceString(price);

    // appel de la fonction de scan de carte
    eel.await_card_scan(price);


    const text = document.getElementById("textWriter");
    const anim = () => {
        text.innerHTML = base
        setTimeout(() => {
            text.innerHTML = base + "."
            setTimeout(() => {
                text.innerHTML = base + ".."
                setTimeout(() => {
                    text.innerHTML = base + "..."
                    setTimeout(() => {
                        anim()
                    }, delay)
                }, delay)
            }, delay)
        }, delay)
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