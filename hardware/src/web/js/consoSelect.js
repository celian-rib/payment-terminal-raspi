/**
 * Nombre de produits affichés par page du caroussel
 */
const productsPerPage = 4;
/**
 * Element du DOM contenant les produits affichés
 */
const pageElements = [];
/**
 * Ensemble des produits en vente
 */
let products = []
/**
 * Indice de la page actuelle du caroussel affichée
 */
let currentPage = 0;
/**
 * Utilisateur courant
 */
let user = undefined;

/**
 * Charge tous les produits en vente
 */
const loadProducts = async () => {
    products = await eel.get_products()()
    console.log("Producst loaded", products);
}

/**
 * @returns Total d'argent que l'utilisateur doit
 */
const getDeptAmount = () => {
    let val = 0;
    user.products.forEach(p => {
        val += p.count * p.product.asso_price;
    })
    return val;
}

/**
 * Ajoute un produit consommé a l'utilisateur
 * @param product 
 */
const addProduct = async (product) => {
    await eel.add_or_remove_user_product(user.card_uid, product.product_id, true)();
    await refreshUserData();
    updateCurrentPageProducts();
}

/**
 * Retire un produit consommé a l'utilisateur
 * @param product 
 */
const removeProduct = async (product) => {
    const validate = await showPopup("Enlever ce produit des produits consommés ?")
    if (!validate)
        return;
    await eel.add_or_remove_user_product(user.card_uid, product.product_id, false)();
    await refreshUserData();
    updateCurrentPageProducts();
}

/**
 * Met à jour l'entièreté des données de l'utilisateur
 */
const refreshUserData = async () => {
    const cardUid = new URLSearchParams(window.location.search).get("cardUid");
    user = await eel.get_user(cardUid)()
    console.log("User loaded", user);
    document.getElementById("assoName").innerHTML = user.first_name || "Admin";
}

/**
 * Met à jour l'affichage du caroussel
 */
const updateCurrentPageProducts = () => {
    const pageProducts = products.filter((_, i) => i >= currentPage * productsPerPage && i <= (currentPage * productsPerPage) + productsPerPage);
    pageElements.forEach((element, index) => {
        if (index >= pageProducts.length) {
            element.style = "visibility: hidden;"
            return;
        }
        itemCountForUser = user.products.find(p => p.product.product_id == pageProducts[index].product_id)?.count ?? 0;
        element.innerHTML = `
            <div class="btn" style='padding: 10px 20px; ${itemCountForUser > 0 ? "opacity: 1;" : "opacity: 0;"}'>- </div>
            <span>
                <p style="color: ${pageProducts[index].color};">${pageProducts[index].name}</p>
                <p>${getPriceString(pageProducts[index].asso_price)}</p>
            </span>
            <span>
                <p style="color: ${pageProducts[index].color};">qte : ${itemCountForUser}</p>
            </span>
            <div class="btn" style="padding: 10px 20px;"> +</div>
        `;
        element.firstElementChild.addEventListener("click", () => removeProduct(pageProducts[index]))
        element.lastElementChild.addEventListener("click", () => addProduct(pageProducts[index]))
        element.style = "visibility: visible;"
    });
    document.getElementById("assoDebt").innerHTML = getPriceString(getDeptAmount());
}

window.onload = async () => {
    await loadProducts();
    await refreshUserData();

    // Setup all page elements (4 items per pages)
    const container = document.getElementsByClassName('itemsContainer')[0];
    for (let i = 0; i < productsPerPage; i++) {
        const node = document.createElement("div");
        node.className += "item";
        container.append(node);
        pageElements.push(node);
    }

    updateCurrentPageProducts();
}

document.getElementById("previousArrow").style = "visibility: hidden;";
// Bouton pour tout rembourser
document.getElementById("resetDebt").addEventListener("click", async () => {
    const del = await showPopup(`Je confirme avoir remboursé ${getPriceString(getDeptAmount())}`)
    if (del) {
        await eel.delete_all_user_products(user.card_uid)()
        await refreshUserData();
        updateCurrentPageProducts();
    }
});

// Changement page caroussel
document.getElementById("nextArrow").addEventListener("click", () => {
    document.getElementById("previousArrow").style = "visibility: visible;";
    currentPage += 1;
    if (currentPage > products.length / productsPerPage - 1)
        document.getElementById("nextArrow").style = "visibility: hidden;";
    if (currentPage > products.length / productsPerPage)
        currentPage = products.length / productsPerPage;
    updateCurrentPageProducts();
})

// Changement page caroussel
document.getElementById("previousArrow").addEventListener("click", () => {
    currentPage -= 1;
    document.getElementById("nextArrow").style = "visibility: visible;"
    if (currentPage == 0)
        document.getElementById("previousArrow").style = "visibility: hidden;";
    if (currentPage < 0)
        currentPage = 0;
    updateCurrentPageProducts();
})
