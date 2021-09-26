const base = "En attente de la carte";
const delay = 200;

window.onload = () => {
    const text = document.getElementById("textWriter");
    const anim = () => {
        text.innerHTML = base
        setTimeout(() => {
            text.innerHTML = base + "."
            setTimeout(() => {
                text.innerHTML = base + ".."
                setTimeout(() => {
                    text.innerHTML = base + "..."
                    setTimeout(() => {
                        anim()
                    }, delay)
                }, delay)
            }, delay)
        }, delay)
    }
    anim()
}