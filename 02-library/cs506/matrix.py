
B = [[4,6],[3,8]]
C = [[6,1,1],[4,-2,5],[2,8,7]]

print(version)

def check_valid(matrix):
    """
    check if this is a vaild matrix
    input a matrix
    raise error if invaild
    """
    if len(matrix) != len(matrix[0]):
        raise ValueError('input matrix must be nxn')

def get_determinant(matrix):
    """
    input a matrix(2D list)
    output the determinant of that matrix (int)
    """
    #check
    check_valid(matrix)

    numN = len(matrix) # a nxn matrix
    if numN <= 0 :
        return None
    if numN == 1:
        return matrix[0][0]
    else:
        local_D = 0
        for i in range(numN):
            recursive_matrix = [[row[a] for a in range(numN) if a != i] for row in matrix[1:]]
            if i % 2 == 0:
                local_D = local_D + matrix[0][i] * get_determinant(recursive_matrix)
            else:
                local_D = local_D - matrix[0][i] * get_determinant(recursive_matrix)
        return local_D

print(get_determinant([[4,6],[3,8]]))
print(get_determinant(C))

    