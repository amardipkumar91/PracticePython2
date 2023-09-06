
# def check_passed_value(list_data, search_data):
#     for index, i in enumerate(list_data):
#         if search_data == i:
#             break
#     return index + 1


# if __name__ == '__main__':
#     data = input()
#     data_split = data.split('##')
#     list_data = data_split[0].split(',')
#     search_data = data_split[1]
#     print (check_passed_value(list_data, search_data))
    
def check_super_hero_power():
    


if __name__ == '__main__':
    data = 'BATMAN:10#SUPERMAN:-5#HANUMAN:4#SPIDERMAN:-22#IRONMAN:6#HULK:9'
    data_split = data.split('#')
    dictt = {}
    for i in data_split:
        ll_split = i.split(':')
        dictt[ll_split[0]] = ll_split[1]

    import pdb;pdb.set_trace()