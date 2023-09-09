async function setForm(link) {
    clearResults()
    document.querySelector('form').innerHTML = await (await fetch(link, {method: 'POST'})).text()
}