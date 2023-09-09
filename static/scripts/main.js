async function requestEquation(event) {
    event.preventDefault()

    clearResults()

    const method = getMethod(),
        equation = getEquation(),
        left = isFloat(getLeft()),
        right = isFloat(getRight()),
        eps = isFloat(getEps())

    if (equation === false){fire('Выберите уравнение'); return}
    if (method === false){fire('Выберите метод'); return}
    if (left === false || right === false || eps === false) {fire('Входные данные должны содержать числа');return}
    if (left >= right) {fire('Правый край должен быть больше левого');return}
    if (eps <= 0) {fire('Эпсилон должен быть больше 0'); return}

    const resp =  await recieveData(await requestData(EQ_LINK, {method, equation, left, right, eps}), extractJSON)


    if (resp === false) return

    setGraph(URL.createObjectURL(await recieveData(await requestData(EQ_GRAPH, {method, equation, left, right, eps}), extractImg)))

    equation_answer(resp, equation, method)
}

async function requestSystem(event) {
    event.preventDefault()

    clearResults()

    const equation = getEquation(),
        x = isFloat(getLeft()),
        y = isFloat(getRight())

    if (equation === false){fire('Выберите уравнение'); return}
    if (x === false || y === false) {fire('Входные данные должны содержать числа');return}

    const resp =  await recieveData(await requestData(SYS_LINK, {equation, x, y}), extractJSON)



    if (resp === false) return

    system_answer(resp, equation)

    setGraph(URL.createObjectURL(await recieveData(await requestData(SYS_GRAPH, {equation, x, y}), extractImg)))

}
