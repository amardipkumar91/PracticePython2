def findBeforeMatrix(after):
    
    before = []
    l_data = []
    for index_i, i in enumerate(after):
        for index_j, j in enumerate(i):
            if index_i == 0 and index_j == 0:
                before.insert(index_j, [j])
                l_data.append(j)
            else:
                if l_data:
                    c_data = sum(l_data)
                    try:
                        before[index_i].append(c_data)
                    except:
                        before.insert(index_i,[c_data])
                    l_data.append(c_data)
    



            



    # Write your code here
    
if __name__ == '__main__':
    

    after_rows = int(raw_input().strip())
    after_columns = int(raw_input().strip())

    after = []

    for _ in xrange(after_rows):
        after.append(map(int, raw_input().rstrip().split()))

    result = findBeforeMatrix(after)

