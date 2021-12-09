import numpy as np
from random import randint, uniform
from decimal import Decimal

def GenSLU(n):
    if n < 0:
        return 0
    matrix = np.eye(n)
    vecAns = np.round(np.random.uniform(-100, 100, n), 0)
    # print(vecAns)
    for i in range(0, 5 * n):
        while True:
            a = randint(0, n-1)
            b = randint(0, n-1)
            k = round(uniform(-1, 1), 0)
            if k == 0:
                continue

            if a != b:
                matrix[a] += matrix[b] * k
                vecAns[a] += vecAns[b] * k

                break

    matrix = matrix.astype(int)
    vecAns = vecAns.astype(int)

    # vecAns = [list(map(int, num) for num in vecAns)]

    return matrix.tolist(), vecAns.tolist()


