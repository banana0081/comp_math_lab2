from storages.jacobians_store import jacobians
import methods.gauss as gauss


def solve(system, x0, y0):
    matrix: list[list[float]]
    errors = [[], []]
    i = 0
    epsilon = 0.01
    inc_x, inc_y = epsilon + 1, epsilon + 1
    while abs(inc_x) > epsilon or abs(inc_y) > epsilon:
        matrix = []
        for j in range(len(jacobians[system])):
            ls = jacobians[system][j]
            matrix.append([])
            matrix[-1].append(ls[0](x0))
            matrix[-1].append(ls[1](y0))
            matrix[-1].append(-system[j](x0, y0))

        inc_x, inc_y = gauss.count_result(matrix)
        errors[0].append(inc_x)
        errors[1].append(inc_y)
        x0 += inc_x
        y0 += inc_y
        i += 1


    print(f'Solution: [{round(x0, 5), round(y0, 5)}]')
    print(f'Pogreshnosty for x: {errors[0]}')
    print(f'Pogreshnosty for y: {errors[1]}')
    print(f'Number of iterations: {i}')
    return {
        'result': {'x': round(x0, 5), 'y': round(y0, 5)},
        'x': errors[0],
        'y': errors[1]
    }