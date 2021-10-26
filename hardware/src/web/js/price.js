var price = 0;
var dynamic_visibility_buttons = [];

var checkDynamicButtonsVisibility = () => {
	dynamic_visibility_buttons.forEach(b => {
		let value = parseInt(parseFloat(b.innerHTML.replace(/\s/g, '')) * 100)
		if (value == 0) value -= 1;
		b.style = `visibility: ${price + value >= 0 ? "visible" : "hidden"};`;
	})
}

/**
 * Fonction appellée lorsque la page est entièrement chargée
 */
window.onload = function () {
	const buttonScans = document.getElementsByClassName('btnPrice');
	const priceText = document.getElementById('value');

	for (let i = 0; i < buttonScans.length; i++) {
		let value = parseInt(parseFloat(buttonScans[i].innerHTML.replace(/\s/g, '')) * 100)
		if (value <= 0)
			dynamic_visibility_buttons.push(buttonScans[i])
		buttonScans[i].addEventListener('click', () => {
			if (value == 0)
				price = 0;
			price += value;
			if (price < 0)
				price = 0;
			priceText.innerHTML = getPriceString(price);
			checkDynamicButtonsVisibility();
		})
	}

	const btnAjout = document.getElementById('ajout');
	if (btnAjout)
		btnAjout.addEventListener('click', () => goToWithParam('goToNfc', '?' + price), false);

	const btnDebit = document.getElementById('debit');
	if (btnDebit)
		btnDebit.addEventListener('click', () => goToWithParam('goToNfc', '?' + -price), false);

	checkDynamicButtonsVisibility();
};