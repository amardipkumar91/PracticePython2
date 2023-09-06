from datetime import datetime
def change_date_form(u_date):
    u_date_split = u_date.split('_')
    split_1 = u_date_split[0]
    split_2 = u_date_split[1]
    date = datetime.strptime(split_1,'%Y%m%d').date()
    time = datetime.strptime(split_2, '%I%M%S').time()
    result = str(datetime.combine(date,time))
    return result
print (change_date_form('20200725_112223'))