def findLargestSquare(M, m, n, maxsize):
    if m == 0 or n == 0:
        return M[m][n], max(maxsize, M[m][n])
    left, maxsize = findLargestSquare(M, m, n - 1, maxsize)
    top, maxsize = findLargestSquare(M, m - 1, n, maxsize)
    diagonal, maxsize = findLargestSquare(M, m - 1, n - 1, maxsize)
    size = 1 + min(min(top, left), diagonal) if M[m][n] else 0
    return size, max(maxsize, size)


if __name__ == '__main__':

    # M = [
    #     [1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 0, 0, 1, 0]
    # ]

    M = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    # M = [
    #     [0, 1, 1, 1],
    #     [1, 1, 0, 1],
    #     [0, 1, 1, 1]
    # ]

    maxsize = findLargestSquare(M, len(M) - 1, len(M[0]) - 1, 0)[1]
    # import pdb;pdb.set_trace()
    print("The area of matrix is :", maxsize * maxsize)
    