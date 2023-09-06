#Find last two remaining elements after removing median of any 3 consecutive elements repeatedly

import statistics

def lastTwoElement(data_list):
    while len(data_list) != 2:
        median_data = statistics.median(data_list[0:3])
        data_list.remove(median_data)
    return data_list

if __name__ == '__main__':
    data = [38, 9, 102, 10, 96,7, 46, 28, 88, 13] 
    last_two_element = lastTwoElement(data)
    print (last_two_element)