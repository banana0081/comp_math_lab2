import storages.equation_store as es
import storages.method_store as ms
import math_util.check_intervals as ci
import graphs.equation_graphic as graph
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg
import methods.newton_system as ns

def extract_equation(data):
    return data['method'], data['equation'], data['left'], data['right'], data['eps']

def solve_equation(data):
    method_num, eq_num, l, r, eps = extract_equation(data)
    return exact_solution(method_num, eq_num, l, r, eps)

def draw_equation(data):
    method_num, eq_num, l, r, eps = extract_equation(data)
    root = exact_solution(method_num, eq_num, l, r, eps)['result']
    ints = ci.check(es.getEquationById(eq_num), l, r)
    output = BytesIO()
    fig = graph.eq(es.getEquationById(eq_num), root, ints[0][0], ints[0][1])
    FigureCanvasAgg(fig).print_png(output)
    return output.getvalue()

def exact_solution(mn, en, l, r, eps):
    ints = ci.check(es.getEquationById(en), l, r)
    if len(ints) > 1:
        raise Exception('На промежутке несколько интервалов: ' + str(ints))
    elif len(ints) == 0:
        raise Exception('На промежутке нет корней')
    ints = ints[0]
    return ms.getMethodById(mn)(es.getEquationById(en), es.getDerivativeById(en), ints[0], ints[1], eps)


def extract_system(data):
    return data['equation'], data['x'], data['y']

def solve_system(data):
    eq_num, l, r = extract_system(data)
    return exact_system_solution(eq_num, l, r)

def exact_system_solution(en, x, y):
    return ns.solve(es.getSystemById(en-1), x, y)

def draw_system(data):
    eq_num, l, r = extract_system(data)
    solution = exact_system_solution(eq_num, l, r)
    output = BytesIO()
    fig = graph.sys(es.getSystemById(eq_num-1)[0], es.getSystemById(eq_num-1)[1], solution['result']['x'], solution['result']['y'])
    FigureCanvasAgg(fig).print_png(output)
    return output.getvalue()



