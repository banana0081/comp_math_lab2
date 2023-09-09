function isFloat(num) {
    const tmp = num.replace(',', '.')
    return ((tmp !== '' && !isNaN(tmp)) || parseFloat(tmp) === 0) ? parseFloat(tmp) : false
}