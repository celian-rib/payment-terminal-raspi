window.onload = function () {
	const urlData = parseURLParams(window.location.href);
	const price = urlData['money'][0];
	const userId = urlData['userID'][0];

	let reason = undefined;
	if (urlData['reason'] !== undefined)
		switch(urlData['reason'][0]) {
			default:
				reason = "Erreur inconnue";
				break;
			case 'NEW_USER_CANT_SPEND':
				reason = "Impossible de dépenser en tant que nouvel utilisateur";
				break;
			case 'NOT_ENOUGH_CURRENCY':
				reason = "La solde du compte n'est pas suffisante";
				break;
		};

	document.getElementById('accountMoney').innerHTML = getPriceString(price);
	document.getElementById('clientNum').innerHTML = userId;

	if (document.getElementById('reasonBug'))
		document.getElementById('reasonBug').innerHTML = reason;
};

if (parseURLParams(window.location.href)['raspberry'] != undefined)
	document.getElementsByTagName('html')[0].style = 'transform: rotate(180deg);'