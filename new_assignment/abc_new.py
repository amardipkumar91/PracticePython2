def foo(matrix):
    import pdb;pdb.set_trace()
    rows = len(matrix)
    cols = len(matrix[0])
    maxsqlen = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                sqlen = 1
                flag = True
                while (sqlen + i ) < rows and sqlen + j < cols and flag:
                    k = j
                    for k in range(sqlen + j):
                        if matrix[i + sqlen][k] == 0:
                            flag = False
                            break
                    k = i
                    for k in range(sqlen + i):
                        if matrix[k][j + sqlen ] == 0:
                            flag = False
                            break
                    if flag:
                        sqlen = sqlen + 1
                if maxsqlen < sqlen:
                    maxsqlen = sqlen
    return maxsqlen * maxsqlen

    # int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
   



if __name__ == '__main__':

    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]

    maxsize = foo(matrix)
    print (maxsize)
   
   
