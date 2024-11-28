
def equal_row_column_pairs(matrix):
    n = len(matrix)
    row_count = {}
    for row in matrix:
        row_tuple = tuple(row)
        row_count[row_tuple] = row_count.get(row_tuple, 0) + 1
    count =0
    for col_index in range(n):
        column_tuple = tuple(matrix[row_index][col_index] for row_index in range(n))
        count += row_count.get(column_tuple, 0)

    return count





matrix = [[3,2,1],[1,7,6],[2,7,7]]
print(equal_row_column_pairs(matrix))


