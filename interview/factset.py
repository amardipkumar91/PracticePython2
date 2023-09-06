# --- group anagram string--------
AA = ['eat', 'tae', 'mun', 'num', 'wer', 'tre', 'etr', 'rwe', 'erw', 'pup']
def group_anagram(A):
    lst = ["".join(sorted(i)) for i in A]
    dictt = dict()
    for index, val in enumerate(lst):
        dictt.setdefault(val, []).append(index)
    result = []
    for key, val in dictt.items():
        result.append([AA [i] for i in val])
    return result
print (group_anagram(AA))

#------------------- group all even in one list and all odd in one----

el = []
print ([el.append(i) for i in range(10)  if i%2 ==0])

#-----------Change all elements of row `i` and column `j` in a matrix to 0 if cell `(i, j)` is 0 -----

def convertRowColumn(mat, M , N, i, j):
    for x in range(N):
        if mat[i][x]:
            mat[i][x] = -1
    for y in range(M):
        if mat[y][j]:
            mat[y][j] = -1
def convert(mat):
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                convertRowColumn(mat, M , N, i, j)
    for i in range(M):
        for j in range(N):
            if mat[i][j] == -1:
                mat[i][j] =0 

if __name__ == '__main__':
    mat = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1]
    ]
    convert(mat)
    for i in mat:
        print (i)