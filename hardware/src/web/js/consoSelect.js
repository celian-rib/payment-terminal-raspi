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
const pageSize = 6;
const pageElements = []

window.onload = () => {
    document.getElementById("previousArrow").style = "visibility: visible;";

    // on prends les 6 premieres pour en 
    // avoir 6 par page
    const pageItems = products.filter((_, i) => i < pageSize);

    // on récupère le container qui vas les accueillir
    const container = document.getElementsByClassName('itemsContainer')[0];
    
    // elements de la premiere page
    pageItems.forEach(item => {
        // on le transforme en div
        const node = document.createElement("div");
        // on l'ajoute au container
        container.append(node);
        // on lui donne le nom de l'élément
        node.innerHTML = item.name;
        // on le caste en bouton
        node.className += "btn";
        pageElements.push(node);
    });
}

document.getElementById("nextArrow").addEventListener("click", () => {
    document.getElementById("previousArrow").style = "visibility: visible;";

    currentPage += 1;
    if (currentPage > products.length / pageSize - 1)
        document.getElementById("nextArrow").style = "visibility: hidden;";
    if (currentPage > products.length / pageSize) {
        currentPage = products.length / pageSize;
    }
    updateItems();
})

document.getElementById("previousArrow").addEventListener("click", () => {
    currentPage -= 1;
    document.getElementById("nextArrow").style = "visibility: visible;"
    if (currentPage = 0)
        document.getElementById("previousArrow").style = "visibility: hidden;";
    if(currentPage < 0)
        currentPage = 0;
    updateItems();
})

const updateItems = () => {
    const pageItems = products.filter((_, i) => i > currentPage * pageSize && i <= (currentPage * pageSize) + pageSize);
    pageElements.forEach((element, index) => {
        if (index < pageItems.length) {
            element.innerHTML = pageItems[index].name;
            element.style = "visibility: visible;"
        } else {
            element.style = "visibility: hidden;"
        }
    })
}