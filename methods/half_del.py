def solve(f, der, left, right, eps):
    a = left; b = right
    itr = []
    while len(itr) < 20:
        x = (a + b) / 2
        delta = abs(a - b)
        itr.append([a, b, x, f(a), f(b), f(x), delta])
        if delta < eps: return {'table': itr, 'result': x}
        if f(a) < 0 and f(x) < 0 or f(a) > 0 and f(x) > 0: a = x
        else: b = x
    return None
