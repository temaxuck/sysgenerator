import numpy as np

def Cram(A, B):
    op = np.linalg.det(A)
    print(op)
    r = list()
    for i in range(len(A)):
        VM = np.copy(A)
        VM[:,i] = B
        r.append(np.linalg.det(VM) / op)
    return r
