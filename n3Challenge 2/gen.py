import os
import sys
import argparse
import string
import random
import csv
from datetime import datetime

now=datetime.now()
indate =  now.strftime("%Y-%m-%d-%H_%M_%S")


def get_random_letter():
    #creating randoms letters 
    len_apphabet = tuple(range(1,11))
    random_no = random.choice(len_apphabet)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(random_no))

def get_random_number():
    #creating randoms numbers 
    return random.randint(0, 99999)

def parse_agrs(args):
    rows = args.rows
    if not rows:
        rows = 50
    output_path = args.output_path
    if not output_path:
        output_path = os.getcwd()
    columns = args.columns
    col_split = columns.split(',')
    column_dict = {}
    
    for i in range(0,len(col_split),2):
        #checking type of argument for each column
        if col_split[i+1] == 'str':
            col_type = str
        elif col_split[i+1] == 'int':
            col_type = int
        else:
            column_dict = {}
            break
        column_dict[col_split[i]] = col_type
    return rows, output_path, column_dict

def get_rows(column_type):
    data = []
    for i in column_type: # if column type is string it will cal random_letter func else random_number func
        if i == str:
            data.append(get_random_letter())
        else:
            data.append(get_random_number())
    return data

def write_csv(rows, output_path, columns):
    keys = [i for i in columns.keys()]
    values = columns.values()
    file_path = output_path + '/'+indate+'.csv' # creating csv file with the current datetime name
    try:
        with open(file_path,'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(keys)
            for i in range(rows):
                # calling function to create each row for csv file
                data = get_rows(values)
                writer.writerow(data)
        return indate
    except Exception as e:
        print(e)
            
if __name__ == '__main__':
    # import pdb;pdb.set_trace()
    # aargparse make easy to write user friendly command-line interface
    parser = argparse.ArgumentParser(description='This program take upto 3 named option and create a output CSV file in your local directory.')
    parser.add_argument('-r','--rows', help='Enter the Row numer else it will take 50', required=False, type=int) #argument one
    parser.add_argument('-o','--output_path', help='Enter the OutPut Path else it will take current directory', required=False) #argument second
    parser.add_argument('-c','--columns', help='Enter the column name ', required=True)  #argument three:- compulsary to pass arugument with column name and its type. ex:- 'Name',str
    args = parser.parse_args()
    rows, output_path, columns = parse_agrs(args)
    if not columns:
        print ("Please Specify the column argument like :- name,str,phone,int")
        sys.exit(1)
    #calling function to create csv and write data into it.
    file_name = write_csv(rows, output_path, columns)
    print(file_name)
   