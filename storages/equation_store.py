from numpy import sin, cos

storage = {
    1: {
        'equation': lambda x: x**3 - 2 * x,
        'derivative': lambda x: 3*x**2 - 2
    },
    2: {
        'equation': lambda x: sin(3*x),
        'derivative': lambda x: 3*cos(3*x)
    },
    3: {
        'equation': lambda x: pow(x, 3) - x + 4,
        'derivative': lambda x: 3*pow(x, 2)-1
    }
}

systems_storage = [
    tuple([lambda x, y: x ** 2 + y ** 2 - 4, lambda x, y: y - 3 * x ** 2]),
    tuple([lambda x, y: sin(x) + y - 1, lambda x, y: -2 * x ** 3 - 4 * y + 5]),
]

def getEquationById(id):
    return storage[id]['equation']

def getDerivativeById(id):
    return storage[id]['derivative']

def getSystemById(id):
    return systems_storage[id]
