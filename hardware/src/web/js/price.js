/**
 * Fonction appellée lorsque la page est entièrement chargée
 */
window.onload = function () {
	let price = 0;

	const buttonScans = document.getElementsByClassName('btnPrice');

	const priceText = document.getElementById('value');

	for (let i = 0; i < buttonScans.length; i++) {
		let value = parseInt(parseFloat(buttonScans[i].innerHTML) * 100)
		buttonScans[i].addEventListener('click', () => {
			if (value == 0)
				price = 0;
			price += value;
			if (price < 0)
				price = 0;
			priceText.innerHTML = getPriceString(price);
		})
	}
	if (document.getElementById('ajout'))
		document
			.getElementById('ajout')
			.addEventListener('click', () => goToWithParam('goToNfc', '?' + price), false);
	if (document.getElementById('debit'))
		document
			.getElementById('debit')
			.addEventListener('click', () => goToWithParam('goToNfc', '?' + -price), false);
};