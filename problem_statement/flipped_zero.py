# def flipped_zero(arr, n,m):
#     print ("start")
#     wl = wr = 0
#     bestwindow = bestL = 0
#     zerocount = 0
#     while wr < n:
#         if zerocount <=m :
#             if arr[wr] == 0:
#                 zerocount += 1
#             wr += 1
#         if zerocount > m:
#             if arr[wl] == 0:
#                 zerocount -= 1
#             wl += 1
#         if (wr -wl > bestwindow) and (zerocount <= m):
#             bestwindow = wr - wl
#             bestL = wl
#     for i in range(0, bestwindow):
#         if arr[bestL + i] == 0:
#             import pdb;pdb.set_trace()
#             print (bestL + i)

def flipped_zero(arr, n, m):
    wr = wl = 0
    bestwindow = bestL = zerocount = 0
    while wr < n:
        if zerocount <= m:
            if arr[wr] == 0:
                zerocount += 1
            wr += 1
        
        if zerocount > m:
            
            if arr[wl] ==0 :
                zerocount -= 1
            wl += 1
        
        if (wr - wl > bestwindow) and (zerocount <=m):
            bestwindow = wr - wl
            bestL = wl
    
    for i in range(0, bestwindow):
        if arr[bestL + i] == 0:
            import pdb;pdb.set_trace()
            print (bestL + i)


if __name__ == '__main__':
    arr = [1,0,1,1,0,0,1,1,1,1]
    n = len(arr)
    m = 2
    flipped_zero(arr, n, m)
