def solve(f, der, left, right, eps):
    itr = []
    x0 = left; x1 = left + 0.001; x2 = 0; k = 0
    while len(itr) < 20:
        x2 = x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1)
        delta = abs(x2 - x1)
        itr.append([x0, x1, x2, f(x2), delta])

        if delta < eps:
            return {'table': itr, 'result': x2}
        k += 1
        x0 = x1
        x1 = x2
    return None