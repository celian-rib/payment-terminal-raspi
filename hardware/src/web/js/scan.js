let buttonMinusCent;
let buttonMinusOne;
let buttonPlusOne;
let buttonPlusCent;

let priceText;
let price = 0;

/**
 * Fonction appellée lorsque la page est entièrement chargée
 */
window.onload = function() {
	buttonMinusCent = document.getElementById('but1');
	buttonMinusOne = document.getElementById('but2');
	buttonPlusOne = document.getElementById('but3');
	buttonPlusCent = document.getElementById('but4');

	priceText = document.getElementById('value');

	buttonMinusCent.addEventListener('click', () => {
		price -= 10;
		if (price < 0) {
			price = 0;
		}
		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonMinusOne.addEventListener('click', () => {
		price -= 100;
		if (price < 0) {
			price = 0;
		}
		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonPlusOne.addEventListener('click', () => {
		price += 100;
		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonPlusCent.addEventListener('click', () => {
		price += 10;
		priceText.innerHTML = getPriceString(price);
	}, false);

	document
		.getElementById('ajout')
		.addEventListener('click', () => goToWithParam('goToNfc', '?' + price), false);
	document
		.getElementById('debit')
		.addEventListener('click', () => goToWithParam('goToNfc', '?' + -price), false);
};