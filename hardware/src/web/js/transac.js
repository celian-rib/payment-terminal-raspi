async function timerAnimation() {
	const element = document.getElementById('timer');
	for (let i = 10; i > 0; i--) {
		element.innerHTML = i;
		await delay(1000);
	}
	goTo(router['goToScan'])
}

window.onload = function () {
	const urlData = parseURLParams(window.location.href);
	const price = urlData['money'][0];
	const userId = urlData['userID'][0];

	let reason = undefined;
	if (urlData['reason'] !== undefined)
		reason = urlData['reason'][0];

	document.getElementById('accountMoney').innerHTML = getPriceString(price);
	document.getElementById('clientNum').innerHTML = userId;

	if (document.getElementById('reasonBug'))
		document.getElementById('reasonBug').innerHTML = reason;

	timerAnimation();
};