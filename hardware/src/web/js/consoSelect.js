const products = [
    { name: "Boisson", price: 60, color: "#f6e58d" },
    { name: "Twix", price: 40, color: "#55efc4" },
    { name: "Bueno", price: 70, color: "#c7ecee" },
    { name: "Smarties", price: 60, color: "#686de0" },
    { name: "PastaBox", price: 220, color: "#fab1a0" },
    { name: "Riz", price: 170, color: "#c7ecee" },
    { name: "Sandwich", price: 170, color: "#c7ecee" },
    { name: "Cafés", price: 40, color: "#778beb" },
    { name: "Lion", price: 40, color: "#ffbe76" },
    { name: "Gauffre Sucre", price: 40, color: "#ffbe76" },
    { name: "Gauffre Choco", price: 50, color: "#e17055" },
    { name: "Bounty", price: 50, color: "#81ecec" },
    { name: "Snickers", price: 50, color: "#e17055" },
    { name: "Chips", price: 70, color: "#c7ecee" },
    { name: "Monster", price: 120, color: "#cf6a87" },
    { name: "PomPote", price: 40, color: "#55efc4" },
    { name: "Bready", price: 70, color: "#c7ecee" },
    { name: "Nestle", price: 60, color: "#f9ca24" },
    { name: "Crunch", price: 60, color: "#a29bfe" },
    { name: "KitKat", price: 60, color: "#a29bfe" },
    { name: "M&Ms", price: 60, color: "#a29bfe" },
    { name: "Dragibus", price: 50, color: "#81ecec" },
    { name: "Caprisun", price: 30, color: "#ffeaa7" },
    { name: "PastaXtrem", price: 370, color: "#f5cd79" },
    { name: "Nouilles", price: 110, color: "#ea8685" },
]

let currentPage = 0;
const pageSize = 4;
const pageElements = [];
let user = undefined;

const showPopup = async (message) => {
    return new Promise((resolve) => {
        const container = document.getElementsByTagName("body")[0];
        const node = document.createElement("div");
        node.className = "modal";
        
        node.innerHTML = `
            <div class="btn outline">${message}</div>
            <div class="btn blue">Annuler</div>
        `;
    
        container.append(node);
        pageElements.push(node);
        node.firstElementChild.addEventListener("click", () => {
            resolve(true);
            node.remove();
        })
        node.lastElementChild.addEventListener("click", () => {
            resolve(false);
            node.remove();
        })
    });
}

const addProduct = async (item, adding) => {
    if (!adding) {
        const validate = await showPopup("Enlever ce produit des produits consommés ?")
        if (!validate)
            return;
    }
    if (user.products[item.name] == undefined)
        user.products[item.name] = 0;
    user.products[item.name] += adding ? 1 : -1;
    if (user.products[item.name] < 0)
        user.products[item.name] = 0;
    const new_dept = await eel.update_debt(user.card_uid, adding ? item.price : -item.price)()
    document.getElementById("assoDebt").innerHTML = getPriceString(new_dept.debt_amount);
    updateItems();
}

const loadUser = async () => {
    const cardUid = new URLSearchParams(window.location.search).get("cardUid");
    user = await eel.get_user(cardUid)()
    user.products = {}
    document.getElementById("assoName").innerHTML = user.first_name || "Admin";
    document.getElementById("assoDebt").innerHTML = getPriceString(user.debt_amount);
}

const updateItems = () => {
    const pageItems = products.filter((_, i) => i >= currentPage * pageSize && i <= (currentPage * pageSize) + pageSize);
    pageElements.forEach((element, index) => {
        if (index >= pageItems.length) {
            element.style = "visibility: hidden;"
            return;
        }
        console.log(JSON.stringify(user.products, null, 2))
        itemCountForUser = user.products[pageItems[index].name] ?? 0;
        element.innerHTML = `
            <div class="btn" style='padding: 10px 20px; ${itemCountForUser > 0 ? "opacity: 1;" : "opacity: 0;"}'>- </div>
            <span>
                <p style="color: ${pageItems[index].color};">${pageItems[index].name}</p>
                <p>${getPriceString(pageItems[index].price)}</p>
            </span>
            <span>
                <p style="color: ${pageItems[index].color};">nb : ${itemCountForUser}</p>
            </span>
            <div class="btn" style="padding: 10px 20px;"> +</div>
        `;
        element.firstElementChild.addEventListener("click", () => addProduct(pageItems[index], false))
        element.lastElementChild.addEventListener("click", () => addProduct(pageItems[index], true))
        element.style = "visibility: visible;"
    })
}

window.onload = async () => {
    await loadUser();
    document.getElementById("previousArrow").style = "visibility: hidden;";
    document.getElementById("resetDebt").addEventListener("click", () => {
        showPopup(`Je confirme avoir remboursé ${getPriceString(user.debt_amount)}`)
    });

    const container = document.getElementsByClassName('itemsContainer')[0];
    for (let i = 0; i < pageSize; i++) {
        const node = document.createElement("div");
        node.className += "item";
        container.append(node);
        pageElements.push(node);
    }
    updateItems();
}

document.getElementById("nextArrow").addEventListener("click", () => {
    document.getElementById("previousArrow").style = "visibility: visible;";
    currentPage += 1;
    if (currentPage > products.length / pageSize - 1)
        document.getElementById("nextArrow").style = "visibility: hidden;";
    if (currentPage > products.length / pageSize)
        currentPage = products.length / pageSize;
    updateItems();
})

document.getElementById("previousArrow").addEventListener("click", () => {
    currentPage -= 1;
    document.getElementById("nextArrow").style = "visibility: visible;"
    if (currentPage == 0)
        document.getElementById("previousArrow").style = "visibility: hidden;";
    if (currentPage < 0)
        currentPage = 0;
    updateItems();
})



