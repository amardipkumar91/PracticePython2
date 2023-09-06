import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    # parser.add_argument('-r','--rows', help='Enter the Row numer else it will take 50', required=False, type=int)
    # parser.add_argument('-o','--output_path', help='Enter the OutPut Path else it will take current directory', required=False)
    parser.add_argument('-c','--columns', help='Enter the column name ', choices=[1,2,3], type=int, nargs='+',required=True)  
    args = parser.parse_args()
    # print (args.columns)
    # import pdb;pdb.set_trace()


    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    # args = parser.parse_args()
    import pdb;pdb.set_trace()
    # print(args.accumulate(args.integers))

    