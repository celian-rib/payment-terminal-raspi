let price = 'loading ...';

const base = 'En attente de la carte';
const animation_tick = 400;

/**
 * Fonction permettant d'annimer le texte de la
 * page de scan nfc durant l'attente du scan
 */
function textAnimation() {
	const text = document.getElementById('textWriter');
	const anim = async () => {
		text.innerHTML = base;
		await delay(animation_tick);
		text.innerHTML = base + '.';
		await delay(animation_tick);
		text.innerHTML = base + '..';
		await delay(animation_tick);
		text.innerHTML = base + '...';
		await delay(animation_tick);
		anim();
	};
	anim();
}

eel.expose(scan_complete);


/**
 * Fonction appellée par python permettant de transférer vers la
 * page de validaton de la commande
 * 
 * @param money quantité d'argent concernée par la transaction
 * @param userID ID de l'utilisateur concerné par la transaction
 * 
 */
function scan_complete(money, userID) {
	goToWithParam('goToValidTransac', '?money=' + money + '&userID=' + userID);
}

eel.expose(scan_cancel);

/**
 * Fonction appellée par python permettant de transférer vers la
 * page d'annulation
 * 
 * @param money quantité d'argent concernée par la transaction
 * @param userID ID de l'utilisateur concerné par la transaction
 * @param reason motif de l'annulation
 * 
 */
function scan_cancel(money, userID, reason) {
	goToWithParam('goToUnvalidTransac', '?money=' + money + '&userID=' + userID + '&reason=' + reason);
}

/**
 * Fonction appelée lorsque la page est entièrement chargée
 */
window.onload = async () => {
	textAnimation(); 
	const urlData = parseURLParams(window.location.href);

	if(Object.keys(urlData)[0] == "target"){
		document.getElementById("priceText").innerHTML = "Scanner carte";
		document.getElementById("priceText").style = "font-size: 30px; letter-spacing: 2px;"
		result = await eel.start_admin_validation()()

		if (result.admin)
			goTo(`${urlData.target[0]}?cardUid=${result.card_uid}`);
		else
			goTo("/index.html");
	} else{
		price = Object.keys(urlData)[0];
		priceText.innerHTML = (price > 0 ? '+' : '') + getPriceString(price);
		// Start transaction on python side
		eel.start_transaction(price);
	}
};

if (parseURLParams(window.location.href)['raspberry'] != undefined)
	document.getElementsByTagName('html')[0].style = 'transform: rotate(180deg);'