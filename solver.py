def solve_LU(A, b):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            s = 0
            for j in range(i):
                s += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - s

        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                L[i][i] = 1
            else:
                s = 0
                for j in range(i):
                    s += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - s) / U[i][i]

    y = [0.0] * n
    for i in range(n):
        s1 = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - s1) / L[i][i]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s2 = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s2) / U[i][i]

    residual = [sum(A[i][j] * x[j] for j in range(n)) - b[i] for i in range(n)]
    #residual_norm = sum(abs(residual[i]) ** 2 for i in range(n)) ** 0.5

    return x