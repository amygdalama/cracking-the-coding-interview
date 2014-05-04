import pprint

def set_zero(matrix):
    """If an element in matrix is 0, set its entire row and column 
    to 0, mutating the original matrix.

    -- matrix: an MxN matrix, i.e. a list of M length N lists
    """

    m = len(matrix)
    n = len(matrix[0])
    rows = [False]*m
    cols = [False]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    test_matrices = (
        [[1]],
        [[0, 1, 2, 3]],
        [[1, 2, 3]],
        [[0, 1, 2], [1, 1, 1], [1, 1, 1]]
        )
    expected = (
        [[1]],
        [[0, 0, 0, 0]],
        [[1, 2, 3]],
        [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
        )
    for i in xrange(len(test_matrices)):
        result = set_zero(test_matrices[i])
        if result == expected[i]:
            print "Success!"
        else:
            print "=========="
            print "Failure!"
            print "Expected:"
            pprint.pprint(expected[i])
            print "Result:"
            pprint.pprint(result)
