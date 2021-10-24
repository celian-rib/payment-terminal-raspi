// tous les produits de la carte, conso asso
const products = [
    { name: "Boisson", price: 60 },
    { name: "Bueno/Bready/Chips", price: 70 },
    { name: "Lion/GSucre", price: 40 },
    { name: "PomPote/Twix", price: 40 },
    { name: "PastaBox", price: 220 },
    { name: "Smarties", price: 60 },
    { name: "Nestle", price: 60 },
    { name: "Crunch/KitKat/M&Ms", price: 60 },
    { name: "Sandwich/Riz", price: 170 },
    { name: "Bounty/Dragibus", price: 50 },
    { name: "GChoco/Snickers", price: 50 },
    { name: "Caprisun", price: 30 },
    { name: "Monster", price: 120 },
    { name: "Cafés", price: 40 },
    { name: "PastaXtrem", price: 370 },
    { name: "Nouilles", price: 110 },
]

let currentPage = 0;
const pageSize = 4;
const pageElements = [];
let user = undefined;

const addProduct = async (item, adding) => {
    const new_dept = await eel.update_debt(user.card_uid, adding ? item.price : -item.price)
    document.getElementById("assoDebt").innerHTML += new_dept;
}

window.onload = async () => {
    
    const cardUid = new URLSearchParams(window.location.search).get("cardUid");
    user = await eel.get_user(cardUid)()
    console.log(user)

    document.getElementById("assoName").innerHTML = user.first_name || "Admin";
    document.getElementById("assoDebt").innerHTML += user.debt_amount;

    document.getElementById("previousArrow").style = "visibility: hidden;";
    document.getElementById("resetDebt").addEventListener("click", () => {
        alert("Confirmer ?")
    }); // FAUT CHANGER AVEC LA DB DU CON

    // on prends les 6 premieres pour en 
    // avoir 6 par page
    const pageItems = products.filter((_, i) => i < pageSize);

    // on récupère le container qui vas les accueillir
    const container = document.getElementsByClassName('itemsContainer')[0];
    
    pageItems.forEach((item, index) => {
        const node = document.createElement("div");
        container.append(node);

        node.innerHTML = `
            <div class="btn" style="padding: 10px 20px;">- </div>
            <p>${item.name}</p>
            <div class="btn" style="padding: 10px 20px;"> +</div>
        `;
        node.firstElementChild.addEventListener("click", () => addProduct(pageItems[index], true))
        node.lastElementChild.addEventListener("click", () => addProduct(pageItems[index], false))
        node.className += "item";
        pageElements.push(node);
    });
}

document.getElementById("nextArrow").addEventListener("click", () => {
    document.getElementById("previousArrow").style = "visibility: visible;";

    currentPage += 1;
    if (currentPage > products.length / pageSize - 2)
        document.getElementById("nextArrow").style = "visibility: hidden;";
    if (currentPage > products.length / pageSize) {
        currentPage = products.length / pageSize;
    }
    updateItems();
})

document.getElementById("previousArrow").addEventListener("click", () => {
    currentPage -= 1;
    document.getElementById("nextArrow").style = "visibility: visible;"
    if (currentPage == 0)
        document.getElementById("previousArrow").style = "visibility: hidden;";
    if(currentPage < 0)
        currentPage = 0;
    updateItems();
})

const updateItems = () => {
    const pageItems = products.filter((_, i) => i >= currentPage * pageSize && i <= (currentPage * pageSize) + pageSize);
    pageElements.forEach((element, index) => {
        if (index < pageItems.length) {
            element.innerHTML = `
                <div class="btn" style="padding: 10px 20px;">- </div>
                <p>${pageItems[index].name}</p>
                <div class="btn" style="padding: 10px 20px;"> +</div>
            `;
            element.firstElementChild.addEventListener("click", () => addProduct(pageItems[index], true))
            element.lastElementChild.addEventListener("click", () => addProduct(pageItems[index], false))
            element.style = "visibility: visible;"
        } else {
            element.style = "visibility: hidden;"
        }
    })
}

