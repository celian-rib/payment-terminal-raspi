function goTo(url) {
    window.location.replace(url);
}

function goToWithParam(pageID, params) {
    const element = router[pageID];
    if (element == null)
        throw "Page doest not exists";
    goTo(element + params);
}

const router = {
    "goToScan": "/pages/scan.html",
    "goToStats": "/pages/stats.html",
    "goToHome": "/index.html",
    "goToNfc": "/pages/nfc.html",
    "goToUnvalidTransac": "/pages/unvalidTransac",
    "goToValidTransac": "/pages/validTransac"
};

for (let route of Object.keys(router)) {

    const element = document.getElementById(route);

    if (element == null) {
        continue;
    }

    element.addEventListener("click", () => goTo(router[route]));
}


    

eel.expose(prompt_alerts);

function prompt_alerts(description) {
    alert(description);
}

eel.expose(get_current_url)

function get_current_url() {
    console.log(window.location.href);
    return window.location.href;
}

function parseURLParams(url) {
    var queryStart = url.indexOf("?") + 1,
        queryEnd = url.indexOf("#") + 1 || url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {},
        i, n, v, nv;

    if (query === url || query === "") return;

    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=", 2);
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);

        if (!parms.hasOwnProperty(n)) parms[n] = [];
        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms;
}

function getPriceString(price) {
    if ((price / 100) % 1 != 0) {
        //decimal number
        return (price / 100) + "0€"
    } else {
        // non decimal number
        return (price / 100) + ".00€"
    }
}