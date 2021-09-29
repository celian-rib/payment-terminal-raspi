
window.onload = async function () {
    const stats = await eel.get_stats()();
    if (stats == null) {
        alert("Stats could not be fetched")
    }
    document.getElementById("totalUsers").innerHTML = "Nombre d'utilisateurs : " + stats.totalUsers
    document.getElementById("totalPrice").innerHTML = "Argent cumulé actuellement : " + stats.totalStoredCurrency + "€"
    document.getElementById("totalScan").innerHTML = "Nombre total de scans : " + stats.totalScanCount
}
