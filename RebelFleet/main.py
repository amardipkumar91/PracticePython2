import mysql.connector as connector
from mysql.connector import Error

def connection():
    """This is for connection configuration funct. 
    If any error will occur in connecting the database this func will throw an error with a console message."""
    
    config = {
        "user": "charu",
        "password": "YARD.lelk7sjgc2besm",
        "host": "130.211.112.62",
        "port": 3306,
        "database": "charu"
    }
    try:
        c = connector.connect(**config)#creating conection
        return c
    except Error as e:
        print("Error while connecting to MySQL", e)#error message
        exit(1)


file_name = "InterviewTest.ale" #filename
def parse_data_from_file():
    """ This func will pase data from file and will return the parsed data"""
    file_obj = open(file_name, 'r')
    all_rows = file_obj.readlines()
    all_data = []
    headers = tuple(all_rows[0].strip().split('\t'))#headers of files
    for row in all_rows[1:]:
        row = row.strip().split('\t')
        all_data.append( tuple(row))
    return headers,all_data#returning parsed data

def queries_on_metadata():
    """This func will insert the data into the database and 
    also have some select queries to fetch desired data"""
    cn = connection()
    cur = cn.cursor()
    headers,rows = parse_data_from_file()
    #storing metadata in the database
    insert_query = 'insert into clm_s_qtake {} values ({})'.format(headers, ",".join(['%s' for i in range(len(headers))])).replace("'", '`')
    cur.executemany(insert_query, rows)
    cn.commit()

    cursor= cn.cursor(dictionary=True)
    #Linking metadata with relevant clip
    query1=("select t1.`clip_id`, t1.`clip_name`,t2.`Start`,t2.`End` from clips as t1 join clm_s_qtake as t2 on t1.`clip_name` = t2.`Name`")
    cursor.execute(query1)
    results = cursor.fetchall()

    #fetchting  total number of clips where the 'Camera' (from the metadata) is equal to 'E'
    query2=("select COUNT(*) from clips as t1 join clm_s_qtake as t2 on t1.clip_name = t2.Name where t2.Camera ='E';")
    cur.execute(query2)
    no_of_clip_results = cur.fetchall()

    #fetching sum of all the clip_size fields (from the clips table) where the 'Camera' is equal to 'A'
    query3=("select sum(t1.`clip_size`) from clips as t1 join clm_s_qtake as t2 on t1.clip_name = t2.Name where t2.Camera ='A';")
    cur.execute(query3)
    sum_of_clip_results = cur.fetchall()

    #fetching  number of clips where the 'Camera' is not one of the first three letters of thealphabet (A, B, C)
    query4=("select COUNT(*) from clips as t1 join clm_s_qtake as t2 on t1.clip_name = t2.Name where t2.Camera not in ('A','B','C');")
    cur.execute(query4)
    no_of_clip_not_abc_results = cur.fetchall()

    cn.close()
    cur.close()
    cursor.close()
    return results,no_of_clip_results,sum_of_clip_results,no_of_clip_not_abc_results
    
if __name__ == '__main__':
    # import pdb;pdb.set_trace()
    results,no_of_clip_results,sum_of_clip_results,no_of_clip_not_abc_results= queries_on_metadata()#calling func to get metadata
    for rows in results:
        [print(key, value) for key, value in rows.items()]#print console output
        print('\n')

    for row in no_of_clip_results:
        print("No. of clips shot by 'E' camera:"+str(row[0]))

    for row in sum_of_clip_results:
        print("Total size shot by 'E' camera:"+str(row[0]))

    for row in no_of_clip_not_abc_results:
        print("No. of clips not ABC:"+str(row[0]))