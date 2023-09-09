const EQ_LINK = '/solve_equation',
    EQ_GRAPH = '/equation_graphic',
    SYS_LINK = '/solve_system',
    SYS_GRAPH = '/system_graphic'

function getLeft() {
    return document.getElementById('left').value
}

function getRight() {
    return document.getElementById('right').value
}

function getEps() {
    return document.getElementById('eps').value
}

function getEquation() {
    try {
        return parseInt(document.querySelectorAll('input[name="eq"]:checked')[0].value)
    } catch(ex) {
        errMsg('Выберите уравнение')
        return false
    }
}

function getMethod() {
    try {
        return parseInt(document.querySelectorAll('input[name="mth"]:checked')[0].value)
    } catch(ex) {
        errMsg('Выберите метод')
        return false
    }
}
