const pageSize = 4;
const pageElements = [];
let products = []
let currentPage = 0;
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

const getDeptAmount = () => {
    let val = 0;
    user.products.forEach(p => {
        val += p.count * p.product.asso_price;
    })
    return val;
}

const addProduct = async (item) => {
    await eel.add_or_remove_user_product(user.card_uid, item.product_id, true)();
    await loadUser();
    updateItems();
}

const removeProduct = async (item) => {
    const validate = await showPopup("Enlever ce produit des produits consommés ?")
    if (!validate)
        return;
    await eel.add_or_remove_user_product(user.card_uid, item.product_id, false)();
    await loadUser();
    updateItems();
}

const loadProducts = async () => {
    products = await eel.get_products()()
    console.log("Producst loaded", products); 
}

const loadUser = async () => {
    const cardUid = new URLSearchParams(window.location.search).get("cardUid");
    user = await eel.get_user(cardUid)()
    console.log("User loaded", user); 
    document.getElementById("assoName").innerHTML = user.first_name || "Admin";
}

const updateItems = () => {
    const pageItems = products.filter((_, i) => i >= currentPage * pageSize && i <= (currentPage * pageSize) + pageSize);
    pageElements.forEach((element, index) => {
        if (index >= pageItems.length) {
            element.style = "visibility: hidden;"
            return;
        }
        itemCountForUser = user.products.find(p => p.product.product_id == pageItems[index].product_id)?.count ?? 0;
        element.innerHTML = `
            <div class="btn" style='padding: 10px 20px; ${itemCountForUser > 0 ? "opacity: 1;" : "opacity: 0;"}'>- </div>
            <span>
                <p style="color: ${pageItems[index].color};">${pageItems[index].name}</p>
                <p>${getPriceString(pageItems[index].asso_price)}</p>
            </span>
            <span>
                <p style="color: ${pageItems[index].color};">qte : ${itemCountForUser}</p>
            </span>
            <div class="btn" style="padding: 10px 20px;"> +</div>
        `;
        element.firstElementChild.addEventListener("click", () => removeProduct(pageItems[index]))
        element.lastElementChild.addEventListener("click", () => addProduct(pageItems[index]))
        element.style = "visibility: visible;"
    });
    document.getElementById("assoDebt").innerHTML = getPriceString(getDeptAmount());
}

window.onload = async () => {
    await loadProducts();
    await loadUser();

    // Setup all page elements (4 items per pages)
    const container = document.getElementsByClassName('itemsContainer')[0];
    for (let i = 0; i < pageSize; i++) {
        const node = document.createElement("div");
        node.className += "item";
        container.append(node);
        pageElements.push(node);
    }

    updateItems();
}

document.getElementById("previousArrow").style = "visibility: hidden;";
document.getElementById("resetDebt").addEventListener("click", async () => {
    const del = await showPopup(`Je confirme avoir remboursé ${getPriceString(user.debt_amount)}`)
    if (del) {
        await eel.delete_all_user_products(user.card_uid)()
        await loadUser();
        updateItems();
    }
});

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



