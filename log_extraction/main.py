import re
import pandas as pd
import os
from datetime import datetime

file1 = 'ingester.txt'
file2 = 'reqr.txt'


def get_data_tradeReference(data):
    time_stamp = re.findall(r'(.*?)INFO', data)[0].strip()
    trade_reference = re.findall(r'tradeReference(.*?),', data)[0]
    trade_reference = re.findall(r'\d+', trade_reference)[0]
    return time_stamp, trade_reference

def get_data_tradeId(data):
    time_stamp = re.findall(r'(.*?)\[ActiveMQ', data)[0].strip()
    trade_id = re.findall(r'tradeId(.*?),', data)[0]
    trade_id =  re.findall(r'\d+', trade_id)[0]
    return time_stamp, trade_id

def read_file(file_name):
    file_obj = open(file_name, 'r')
    reader = file_obj.readlines()
    file_data = []
    for data in reader:
        if 'tradeId' in data:
            time_stamp, trade_reference = get_data_tradeId(data)
        else:   
            time_stamp, trade_reference = get_data_tradeReference(data)
        file_data.append([time_stamp, trade_reference])
    file_obj.close()
    return file_data
    
if __name__ == '__main__':
    all_file = [file1, file2]
    for each_file in all_file:
        data = read_file(each_file)
        fileName = os.path.splitext(each_file)[0]
        file_obj = pd.DataFrame(data, columns=['TimeStamp', 'Trade'])
        file_obj.to_csv(fileName+'.csv')
        
    csv_file1 = 'ingester.csv'
    csv_file2 = 'reqr.csv'
    df1 = pd.read_csv(csv_file1)
    df1 = df1.sort_values(by=['Trade'])

    df2 = pd.read_csv(csv_file2)
    df2 = df2.sort_values(by=['Trade'])
    final_output = []
    for d1, d2 in zip(df1.values, df2.values):
        time_split = d1[1].split()
        ingerster_date = time_split[0]
        ingester_time = time_split[1]
        
        t1 = datetime.strptime(ingester_time, '%H:%M:%S.%f')
        t2 = datetime.strptime(d2[1], '%H:%M:%S.%f')
        
        if t1 > t2:
            elapsetime = t1 - t2
            elapsetime_milisecond = elapsetime.total_seconds() * 1000
            start_time =  ingerster_date+ " "+ str(t2.time())
            end_time = ingerster_date + " "+ str(t1.time())
            
        else:
             elapsetime = t2 - t1
             elapsetime_milisecond = elapsetime.total_seconds() * 1000
             start_time = ingerster_date + " "+str(t1.time())
             end_time = ingerster_date + " "+str(t2.time())
        trade = d1[2]
        if d1[2] == d2[2]:
            final_output.append([ trade,start_time, end_time, elapsetime_milisecond])
        else:
            final_output.append([ trade,"00-00-0000 00:00:00", "00-00-0000 00:00:00", '00000'])
    final_file_obj = pd.DataFrame(final_output, columns=['Trade', 'StartTime', 'EndTime', 'ElapseTime'])
    final_file_obj.to_csv('FinalResult.csv')        
    print ("-------Done-----")
