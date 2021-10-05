window.onload = async function () {
	const histo = await eel.get_historic()();
	if (histo == null) {
		alert('Historic could not be fetched');
	}

    const body = document.getElementsByClassName('histoContainer')[0];
    const template = document.getElementById('template');
    histo.forEach(scan => {
        const scanCard = template.cloneNode(true);
        body.appendChild(scanCard)
        document.getElementById('numClient').innerHTML = scan.id;
        document.getElementById('priceHisto').innerHTML = getPriceString(scan.currency_amount);
    });
    
    template.remove()
};
