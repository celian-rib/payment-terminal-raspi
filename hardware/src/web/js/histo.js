window.onload = async function () {
	const histo = await eel.get_historic()();
	if (histo == null) {
		alert('Historic could not be fetched');
	}

	console.log(histo);
	const container = document.getElementsByClassName('histoContainer')[0];
	histo.forEach((scan, index) => {
		const scanDate = new Date(scan.date);
		const timeStr = getDateString(scanDate);
		const node = document.createElement("div");
		node.setAttribute('class', 'histoTemplate');
		if (scan.transaction_status != "ACCEPTED")
			node.style = "background-color: #b36060;"
		node.innerHTML = `
            <div>
                <p>${scan.user.user_id}</p>
                <img src="../img/user.png" />
                <p>${scan.user.first_name ?? "--"}</p>
            </div>
            <p style="font-size: 11px;">${timeStr}</p>
            <p>${getPriceString(scan.currency_amount)}</p>
        `;
		container.append(node);
	});
};

function getDateString(scanDate) {
	const diff = new Date() - scanDate;
	const diffDays = Math.floor(diff / 86400000); // days
	const diffHrs = Math.floor((diff % 86400000) / 3600000); // hours
	const diffMins = Math.round(((diff % 86400000) % 3600000) / 60000); // minutes
	if (diffDays + diffHrs + diffMins == 0)
		return "Il y a moins d'une minute"
	if (diffDays + diffHrs == 0)
		return `Il y a ${diffMins} min`;
	if (diffDays == 0)
		return `Il y a ${diffHrs} h et ${diffMins} min`
	return `Il y a ${diffDays}j ${diffHrs}h ${diffMins} min`
}
