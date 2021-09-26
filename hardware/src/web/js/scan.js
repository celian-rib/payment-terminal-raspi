let buttonMinusCent;
let buttonMinusOne;
let buttonPlusOne;
let buttonPlusCent;

let priceText;

let price = 0;

window.onload = function() {

    buttonMinusCent = document.getElementById("but1");
    buttonMinusOne = document.getElementById("but2");
    buttonPlusOne = document.getElementById("but3");
    buttonPlusCent = document.getElementById("but4");

    priceText = document.getElementById("value");

    buttonMinusCent.addEventListener("click", () => {
        price -= 10;
        if (price < 0) {
            price = 0;
        }
        showPrice(price);
    }, false);

    buttonMinusOne.addEventListener("click", () => {
        price -= 100;
        if (price < 0) {
            price = 0;
        }
        showPrice(price);
    }, false);

    buttonPlusOne.addEventListener("click", () => {
        price += 100;
        showPrice(price);
    }, false);

    buttonPlusCent.addEventListener("click", () => {
        price += 10;
        showPrice(price);
    }, false);
};

const showPrice = (price) => {
    if ((price / 100) % 1 != 0) {
        //decimal number
        priceText.innerHTML = (price / 100) + "0€"
    } else {
        // non decimal number
        priceText.innerHTML = (price / 100) + ".00€"
    }
}