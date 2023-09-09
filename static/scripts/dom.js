function generate_tbody(answer) {
    let to_fill = ''
    to_fill += '<tbody>'
    for (let i = 0; i < answer.length; i++) {
        to_fill += '<tr>'
        to_fill += `<td>${i}</td>`
        for (let j = 0; j < answer[0].length; j++) {
            to_fill += `<td>${parseFloat(answer[i][j]).toFixed(3)}</td>`
        }
        to_fill += '</tr>'
    }
    to_fill += '</tbody>'
    return to_fill
}

function equation_answer(json, eq, method) {
    const place = document.querySelector('.table'),
        result_place = document.querySelector('.result')
    let equation = '<div>',
        result = '<div>',
        iter = '<div>'


    place.innerHTML = ''

    switch(eq) {
        case 1:
            equation += 'x^3-2x'
            break
        case 2:
            equation += 'sin(3x)'
            break
        case 3:
            equation += 'x^3-x+4'
            break
        default:
            errMsg('error')
    }
    equation += '</div>'

    result += `x=${parseFloat(json.result).toFixed(3)}</div>`

    iter += '<table style="width: 80%; table-layout: fixed;">'
    iter += '<thead>'
    iter += '<tr>'
    switch(method) {
        case 1:
            iter += '<th>№</th>'
            iter += '<th>a</th>'
            iter += '<th>b</th>'
            iter += '<th>x</th>'
            iter += '<th>F(a)</th>'
            iter += '<th>F(b)</th>'
            iter += '<th>F(x)</th>'
            iter += '<th>delta</th>'
            break
        case 2:
            iter += '<th>№</th>'
            iter += '<th>x_{i-1}</th>'
            iter += '<th>x_{i}</th>'
            iter += '<th>x_{i+1}</th>'
            iter += '<th>f(x_{i+1})</th>'
            iter += '<th>delta</th>'
            break
        case 3:
            iter += '<th>№</th>'
            iter += '<th>x_{i}</th>'
            iter += '<th>x_{i+1}</th>'
            iter += '<th>phi(x_{i+1})</th>'
            iter += '<th>f(x_{i+1})</th>'
            iter += '<th>delta</th>'
            break
        default:
            errMsg('error')
    }
    iter += '</tr>'
    iter += '</thead>'
    iter += generate_tbody(json.table)
    iter += '</table>'
    iter += '</div>'

    result_place.innerHTML = equation + result
    
    place.innerHTML = iter


    return json.result
}

function system_answer(data, equation) {
    const place = document.querySelector('.table'),
        result_place = document.querySelector('.result')
    let iter = '<div><table style="table-layout: fixed; width: 50%;"><thead><tr><th>№</th><th>dx</th><th>dy</th></tr></thead>'
    const table = []
    for (let i = 0; i < data.x.length; i++) {
        table.push([data.x[i], data.y[i]])
    }
    iter += generate_tbody(table)
    iter += '</table></div>'

    let eq = ''
    switch (equation) {
        case 1:
            eq += '{ x^2 + y^2 - 4;  y - 3x^2 }'
            break
        case 2:
            eq += '{ sin(x) + y - 1; -2x^3 - 4y + 5 }'
            break
        default:
            errMsg('error')
    }

    place.innerHTML = iter
    result_place.innerHTML = `Point: (${data.result.x}, ${data.result.y}); system: ${eq}`
}

function clearResults() {
    document.querySelector('.graph').innerHTML = ''
    document.querySelector('.result').innerHTML = ''
    document.querySelector('.table').innerHTML = ''
}

function setGraph(src) {
    const image = new Image()
    image.src = src
    document.querySelector('.graph').innerHTML = ''
    document.querySelector('.graph').appendChild(image)
}

function fire(msg) {
    if (document.getElementById('my-alert')) return
    const div = document.createElement('div')
    div.setAttribute('id', 'my-alert')
    div.setAttribute('style', 'position: fixed; min-width: 300px; max-width: 500px; top:50%; left:50%;transform: translate(-50%, -50%);background-color: #323232; color: #eee;border: 2px solid #eee; border-radius: 10px;z-index: 10000; text-align: center; padding: 20px; user-select: none; cursor: pointer;')
    div.innerHTML = msg + '<br> <br>'
    const button = document.createElement('button')
    button.innerHTML = 'OK'
    button.setAttribute('class', 'player-but')

    button.addEventListener('click', () => {
        document.querySelector('body').removeChild(div)
    })
    div.appendChild(button)
    document.querySelector('body').appendChild(div)
}