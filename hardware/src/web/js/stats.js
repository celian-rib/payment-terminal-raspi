
window.onload = function () {
    fetch("http://localhost:5000/api/stats", {            
        method: 'GET',
        mode: 'no-cors',
        headers: {
            'x-access-tokens': 'EcZuVpPHVYvTCfwYFhqk5XXDyP2rzdHuSH4bP36UA2'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}
