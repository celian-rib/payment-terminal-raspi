window.onload = function() {
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
};

if (parseURLParams(window.location.href)['raspberry'] != undefined)
    document.getElementsByTagName('html')[0].style = 'transform: rotate(180deg);'