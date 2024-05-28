from solver import solve_LU


def lagrange_basis(x, i, x_values):
    result = 1
    xi = x_values[i]
    n = len(x_values)
    for j in range(n):
        if i != j:
            xj = x_values[j]
            result *= (x - xj) / (xi - xj)
    return result

def lagrange_interpolation(x_values, y_values, num_points):
    x_min, x_max = min(x_values), max(x_values)
    x_inter = [x_min + i * (x_max - x_min) / (num_points - 1) for i in range(num_points)]
    y_inter = []

    for x in x_inter:
        total = 0
        n = len(x_values)
        for i in range(n):
            yi = y_values[i]
            total += yi * lagrange_basis(x, i, x_values)
        y_inter.append(total)

    return x_inter, y_inter

def select_nodes(x, y, num_nodes):
    step = len(x) // (num_nodes - 1)
    indices = [i * step for i in range(num_nodes - 1)] + [len(x) - 1]
    x_values = [x[i] for i in indices]
    y_values = [y[i] for i in indices]
    return x_values, y_values

#source for splines:
# https://www.bragitoff.com/2018/02/cubic-spline-piecewise-interpolation-c-program/
def create_spline_matrix(x, y):
    n = len(x) - 1
    h = [x[i] - x[i - 1] for i in range(1, n + 1)]

    A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]

    for i in range(1, n):
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        A[i][i - 1] = h[i - 1]
        b[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    A[0][0] = 1
    A[-1][-1] = 1

    return A, b

def create_equation(x, y, s):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]

    variables = []
    for i in range(n):
        a = (s[i + 1] - s[i]) / (6 * h[i])
        b = s[i] / 2
        c = (y[i + 1] - y[i]) / h[i] - h[i] * (s[i + 1] + 2 * s[i]) / 6
        d = y[i]
        variables.append((a, b, c, d, x[i]))

    return variables

def interpolation_splines(x, y, num_points):
    A, b = create_spline_matrix(x, y)
    s = solve_LU(A, b)
    s = [0] + s + [0]

    variables = create_equation(x, y, s)
    x_inter = []
    y_inter = []

    for i in range(len(x) - 1):
        x_range = [x[i] + j * (x[i + 1] - x[i]) / (num_points - 1) for j in range(num_points)]
        for x_val in x_range:
            a, b, c, d, x0 = variables[i]
            y_val = a * (x_val - x0) ** 3 + b * (x_val - x0) ** 2 + c * (x_val - x0) + d
            x_inter.append(x_val)
            y_inter.append(y_val)

    return x_inter, y_inter
