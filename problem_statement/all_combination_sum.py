import itertools
def find_minimum_no_friends(balloons_list, n):
    # all_combination = []
    # for i in range(len(balloons_list), 0, -1):
    #     import pdb;pdb.set_trace()
    #     for seq in itertools.combinations(balloons_list, i):
    #         if sum(seq) == n:
    #             all_combination.append(seq)

    all_combin ation = [seq for i in range(len(balloons_list), 0, -1) for seq in itertools.combinations(balloons_list, i) if sum(seq) == n]
    min_len_of_combinations = min([len(i) for i in all_combination])
    return min_len_of_combinations

if __name__ == '__main__':
    print ("Enter the sum that you want")
    n = int(input())
    print ("Enter the all 6 friends balloons")
    balloons_list = []
    for i in range(6):
        balloons_list.append(int(input()))
    min_len_of_combinations = find_minimum_no_friends(balloons_list, n)
    print (min_len_of_combinations)