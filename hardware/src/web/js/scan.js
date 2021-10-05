/**
 * Fonction appellée lorsque la page est entièrement chargée
 */
window.onload = function() {
	let price = 0;

	const buttonMinusCent = document.getElementById('but1');
	const buttonMinusOne = document.getElementById('but2');
	const buttonPlusOne = document.getElementById('but3');
	const buttonPlusCent = document.getElementById('but4');
	const buttonIsZero = document.getElementById('butIsZero');
	const buttonPlusFive = document.getElementById('butPlusFive');
	const buttonPlusTen = document.getElementById('butPlusTen');
	const buttonPlusTwenty = document.getElementById('butPlusTwenty');

	const priceText = document.getElementById('value');

	buttonIsZero.addEventListener('click', () => {
		price = 0;

		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonPlusFive.addEventListener('click', () => {
		price += 500;

		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonPlusTen.addEventListener('click', () => {
		price += 1000;

		priceText.innerHTML = getPriceString(price);
	}, false);

	buttonPlusTwenty.addEventListener('click', () => {
		price += 2000;

		priceText.innerHTML = getPriceString(price);
	}, false);

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