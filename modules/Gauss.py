from Generator import GenSLU

def Gauss(matrix, solvec):
    for i in range (len(matrix)):
        matrix[i].append(solvec[i])

    resultVector = []
    duplicateMatrix = matrix.copy()
    for i in range(len(matrix) - 1):
        m = []
        for j in range(i + 1, len(matrix[i]) - 1):
            m.append(duplicateMatrix[j][i] / duplicateMatrix[i][i])
        for j in range(i + 1, len(matrix)):
            for k in range(i, len(matrix[i])):
                duplicateMatrix[j][k] -= duplicateMatrix[i][k] * m[j - i - 1]
    for i in range(len(matrix) - 1, -1, -1):
        count = len(resultVector) - 1
        resultX = duplicateMatrix[i][len(matrix[i]) - 1] / duplicateMatrix[i][i]
        j = len(matrix[i]) - 2
        while j > i:
            resultX -= duplicateMatrix[i][j] * resultVector[count] / duplicateMatrix[i][i]
            j -= 1
            count -= 1
        resultVector.insert(0, resultX)
    return resultVector

def gauss(matrix, solvec):
    for i in range (len(matrix)):
        matrix[i].append(solvec[i])

    A = matrix
    m = len(A)
    assert all([len(row) == m + 1 for row in A[1:]]), "Matrix rows have non-uniform length"
    n = m + 1
    
    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # Check for singular matrix
        assert A[i_max][k] != 0, "Matrix is singular!"
        
        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]

        
        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0
    
    # Solve equation Ax=b for an upper triangular matrix A         
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x


matrix, solvec = GenSLU(3)
print(matrix)
print(solvec)
print('\n\n', gauss(matrix, solvec))
print('\n\n', Gauss(matrix, solvec))
