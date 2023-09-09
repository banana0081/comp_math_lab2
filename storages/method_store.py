import methods.secant_method as sm
import methods.half_del as hdm
import methods.simple_iteration as sim

equation_methods = {
    1: hdm.solve,
    2: sm.solve,
    3: sim.solve
}

def getMethodById(id):
    return equation_methods[id]
