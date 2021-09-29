window.onload = function() {
    const urlData = parseURLParams(window.location.href);
    const price = urlData["money"][0];
    const userId = urlData["userID"][0];

    document.getElementById("accountMoney").innerHTML = getPriceString(price);
    document.getElementById("clientNum").innerHTML = userId;
}