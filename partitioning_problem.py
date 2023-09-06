
def get_sublist_combination(arr, half, start, end, index, len_lst, sum_lst): 
    if index == len_lst // 2: 
        curr_sum = sum(half) 
        if (curr_sum + curr_sum == sum_lst): 
            return True 
        else:  
            return False
    i = start 
    while i <= end and (end - i + 1) >= (len_lst // 2 - index): 
        half[index] = arr[i] 
        if get_sublist_combination(arr, half, i + 1, end, index + 1, len_lst, sum_lst): 
            return True
        i += 1
    return False

def check_partitioned(lst, len_lst): 
    sum_lst = sum(lst)
    if sum_lst % 2 != 0: 
        return False
    half = [0] * (len_lst // 2) 
    start = 0
    end = len_lst - 1
    index = 0

    return get_sublist_combination(lst, half, start, end, index, len_lst, sum_lst ) 
    
if __name__ == "__main__": 
    lst = []
    no_of_element = int(input("Enter number of elements : "))
    for i in range(0, no_of_element): 
        ele = int(input()) 
        lst.append(ele)
    
    print ("Your list is", lst)
    len_lst = len(lst) 
    if check_partitioned(lst, len_lst): 
        print("it is partitioned") 
    else: 
        print("it is not partitioned") 