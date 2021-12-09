from fractions import Fraction
def iteration(A,B,eps):

    n = len(B)
    x = [[0,0,0,0,0]]
    global k
    k = 0

    while True:

        x.append(list(range(n)))
        k += 1

        for i in range(n):
            x[k][i] = B[i]/A[i][i]
            for j in range(n):
                if j == i: continue
                x[k][i] -= (A[i][j] * x[k-1][j])/A[i][i]

        #print(x[k])

        for i in range(n):
            if abs(x[k][i] - x[k-1][i]) <= eps:
                return x[k]
            else:
                break


def seidel(A,B,eps):

    n = len(B)
    x = [[0,0,0,0,0]]
    global k
    k = 0

    while True:

        x.append(list(range(n)))
        k += 1

        for i in range(n):
            x[k][i] = B[i]/A[i][i]
            for j in range(i+1,n):
                #if j == i: continue
                x[k][i] -= (A[i][j] * x[k-1][j])/A[i][i]
            for j in range(i):
                #if j == i: continue
                x[k][i] -= (A[i][j] * x[k][j])/A[i][i]

        #print(x[k])

        for i in range(n):
            if abs(x[k][i] - x[k-1][i]) <= eps:
                return x[k]
            else:
                break


def dissLU(a):

    n = len(a)

    l = [[0]*n for i in range(n)]
    u = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0
            if i <= j:
                u[i][j] = a[i][j]
                for k in range(i):
                    s += l[i][k] * u[k][j]
                u[i][j] -= s
                if i==j: l[i][j] = 1

            else:
                l[i][j] = a[i][j]
                for k in range(j):
                    s += l[i][k] * u[k][j]
                l[i][j] = (l[i][j] - s) / u[j][j]
    lu = []
    lu.append(l)
    lu.append(u)
    return lu

'''
def dissol(M):

    n = len(M)

    U = M

    L = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            L[j][i] = U[j][i]/U[i][i]

    for k in range(1, n):
        for i in range(k-1,n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]

        for i in range(k, n):
            for j in range(k-1,n):
                U[i][j] = U[i][j]-L[i][k-1] * U[k-1][j]

    lu = []
    lu.append(L)
    lu.append(U)
 #   U = M
    return U
    '''

def solLU(A,B):
    n = len(A)

    lu = dissLU(A)
    l = lu[0]
    u = lu[1]

    Y = list(range(n))
    X = list(range(n))

    for i in range(n):
        Y[i] = B[i]
        for k in range(i):
            Y[i] -= l[i][k]*Y[k]

    for i in range(n-1,-1,-1):
        X[i] = Y[i]
        for k in range(i+1,n):
            X[i] -= u[i][k]*X[k]
        X[i] /= u[i][i]

    return X

def reversed(A):

    n = len(A)
    R = [[0]*n for i in range(n)]
    #print(R)
    for i in range(n):
        B = [0]*n
        B[i] = 1
        X = solLU(A,B)
        for j in range(n):
            R[j][i] = X[j]

    return R

def multiply(A,B):
    n = len(A)
    C = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for r in range(n):
                C[i][j] += A[i][r] * B[r][j]
            C[i][j] = round(C[i][j])
    return C

def proverk(A,X):
    n = len(X)

    B = [0] * n

    for i in range(n):
        for j in range(n):
            B[i] += A[i][j] * X[j]

    return B

if __name__ == '__main__':

    A = [[56,3,1,1,2],
        [2,48,3,1,1],
        [3,3,8,3,1],
        [1,2,2,56,3],
        [3,3,2,1,40]]

    B = [61,96,6,112,-31]

    print("Matrix A:")

    for i in range(5):
        print(A[i])

    print('\nMatrix B:\n',B)

    print("\nSeidel's method:")

    X1 = seidel(A,B,0.000001)
    for i in range(len(X1)):
        print(X1[i])

    print('\n with ',k,' iterations\n')

    print("\nIteration's method:")

    X1 = iteration(A,B,0.000001)
    for i in range(len(X1)):
        print(X1[i])

    print('\n with ',k,' iterations\n')

    print("\nLU method:")

    X = solLU(A,B)
    for i in range(len(X)):
        print(X[i])

    print('\n\n')

    print("\nCheck:")

    Ch = proverk(A,X)
    for i in range(len(Ch)):
        print(Ch[i])

    print('\n\n')


#    A = [[3, 2, 4], [5, 9, 0], [6, 0, 1]]

    print('\nReversed matrix:')
    R = reversed(A)
    for i in range(len(R)):
        print(R[i])

    print('\n\n')

    print("Checking our reversed matrix:")
    C = multiply(A,R)
    for i in range(len(C)):
        print(C[i])

#    print('bruh',Fraction(C[0][2]),'bruh', round(C[0][2],10))



