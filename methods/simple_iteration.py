def solve(f, der, left, right, eps):
    solution_table = []
    equation = f
    derivative = der

    a_der = derivative(left); b_der = derivative(right)
    l = -1/max(a_der, b_der)
    phi = lambda x: x + l * equation(x)
    phi_der = lambda x: 1 + l * derivative(x)

    start = left
    q = abs(phi_der(start))
    while start < right:
        if q < abs(phi_der(start)):
            q = abs(phi_der(start))
        start += 0.01

    if q > 1:
        raise Exception('Достаточное условие сходимости не выполнено')

    x0 = left
    x1 = 0
    k = 0
    while k < 6:
        x1 = phi(x0)
        criteria = abs(x1 - x0)

        solution_table.append([x0, x1, phi(x1), equation(x1), criteria])

        if criteria < eps:
            return {'table': solution_table, 'result': x1}

        k += 1
        x0 = x1
    return {'table': solution_table, 'result': x1}
