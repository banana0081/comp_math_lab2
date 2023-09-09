from storages.equation_store import systems_storage
from math import cos

jacobians = {
    systems_storage[0]: [
        [lambda x: 2 * x, lambda y: 2 * y],
        [lambda x: -6 * x, lambda y: 1]
    ],
    systems_storage[1]: [
        [lambda x: cos(x), lambda y: 1],
        [lambda x: -6 * x ** 2, lambda y: -4]
    ],
}