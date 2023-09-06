from datetime import datetime
import pandas as pd
import numpy as np


def Remove_blank_row():
    datestring = datetime.strftime(datetime.now(), ' %d%m%Y')
    ppath = '/Users/amardip.kumar/Documents/PracticePython/Alba_test.xlsx'

    df = pd.read_excel(ppath)
    # import time
    # import datetime
    df = df.iloc[7:]
    # print(df)
    # print(df.head(5))
    # print(df.columns)
    # print(df[['Region','Vint.','Description']])
    # print(df.iloc[3:5])
    # print(df.iloc[1,3])
    # for index, row in df.iterrows():
    # print(index,row)
    #   print(index, row['Vint.'])
    # df=df.iloc[1:]
    # for finding specific data in dataset
    
    # print(df.sort_values('Description',ascending=False))
    # df['Total']=df['Vint.']+df['Price per case exc. VAT']
    # print(df.head(5))
    # df=df.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
    # df=df.dropna(how='all')
    # df[['packk','sizee']] = df.Format.str.split("x",expand=True)
    # df['packk']=pd.to_numeric(df.packk)
    # #print(df[['packk','sizee']])
    # df["sizee"]= df["sizee"].replace("cl", "")
    # df["sizee"]= df["sizee"].replace("L", "00")
    # df['Qty']=0
    # df['Pack']=0
    # df['Size']=0
    # df['Price']=0
    # df['CI']=0
    #
    # #df.loc[(df['Cs.']>=1),'Qty']=df.loc[(df['Cs.'])+(df['Btls.'])]
    # #df['Qty']=0
    # #df['Qty']=df.where(df['Cs.']>1,df['Cs.']+['Btls.'],"")
    # #df['Pack']=df['packk']
    # df.loc[df['Cs.']>=1,['Pack']]=df['packk']
    # df.loc[df['Cs.']>=1,['Qty']]=df['Cs.']+df['Btls.']/df['Pack']
    # #df.loc[df['Cs.']>=1,['Pack']]=df['packk']
    # df.loc[df['Cs.']>=1,['Price']]=df['Price per case exc. VAT']
    #
    # df['Size']=df['sizee']
    # df.loc[df['Cs.']<=0,['Qty']]=df['Btls.']
    # df.loc[df['Cs.']<=0,['Pack']]=1
    # df.loc[df['Cs.']<=0,['Price']]=df['Price per case exc. VAT']/df['packk']
    # df.Qty = df.Qty.apply(int)
    # #df['Qty']=round(df['Qty'],0)
    #
    # print(df.loc[:, ['Qty','Pack','Size','Price','CI']].head(10))
    #
    # #print(df.iloc[:, [16,20]])
    # #print(df['sizee'])
  
    # # new data frame with split value columns
    # #new_df = df["Format"].str.split("x", n=1, expand=True)
    # # making separate first name column from new data frame
    # #df["Pack"] = new[0]
    # # making separate last name column from new data frame
    # #df["bt_size"] = new[1]
    # # Dropping old Name columns
    # #data.drop(columns=["Name"], inplace=True)
    # #print(df.head(10))
    # #print(df)
    # #print(df[:,5,16:19])
    # #print(df)
    # #df.to_excel('final.xlsx')
    #
    #
    # #TodaysDate = datetime.strftime(datetime.now().date(), ' %Y_%m_%d')
    # #TodaysDate = pd.datetime.now().date()
    # #excelfilename = TodaysDate +".xlsx"

    datestring = datetime.strftime(datetime.now(), ' %d%m%Y')
    # wb.save('AllData' + datestring + '.xlsm')

    # df.to_excel(r'C:\Users\harendra.gaur\Desktop\Baj_pt\' & excelfilename, index=True)

    df.to_excel('/Users/amardip.kumar/Documents/PracticePython/Alba_test.xlsx',
                index=True, header=False)
    # #Don't forget to add '.xlsx' at the end of the path
    #
    # print("Headers are removed & file is saved successfully")


def List_processing():
    datestring = datetime.strftime(datetime.now(), ' %d%m%Y')
    path = '/Users/amardip.kumar/Documents/PracticePython/Alba_test.xlsx'

    df = pd.read_excel(path)
    # import time
    # import datetime
    # df.style.set_table_styles([dict(selector="th", props=[('max-width', '50px')])])

    # print(df.head(5))
    # print(df.columns)
    # print(df[['Region','Vint.','Description']])
    # print(df.iloc[3:5])
    # print(df.iloc[1,3])
    # for index, row in df.iterrows():
    # print(index,row)
    #   print(index, row['Vint.'])
    # df=df.iloc[3:]

    # for finding specific data in dataset
   
    # print(df.sort_values('Description',ascending=False))
    # df['Total']=df['Vint.']+df['Price per case exc. VAT']
    # print(df.head(5))
    # df=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    # df=df.dropna()
    # df = df.dropna(subset=['Format','Cs.'])
    # df[['packk', 'sizee']] = df.Format.str.split("x", expand=True)

    # Change Column name
    df.rename(
        columns={'Cs': 'Casee', 'Bt': 'Bottlee', 'Size': 'Sizee', 'GBP Sell': 'Case Price', 'GBP/bt': 'Bottle Price'},
        inplace=True)
    # df['Casee'] = pd.to_numeric(df.Casee)

    ## df['packk'] = pd.to_numeric(df.packk)
    # # df['Cs'] = df['Cs'].str.replace('-', '')
    df['Sizee'] = df['Sizee'].str.replace('cl', "")
    df['Sizee'] = pd.to_numeric(df.Sizee)
    # # print(df[['packk','sizee']])
    df["Casee"] = df["Casee"].replace("-", 0)
    df["Bottlee"] = df["Bottlee"].replace("-", 0)
    # df["Sizee"]= df["Sizee"].replace("cl", '')
    #

    df['Qty'] = 0
    df['Pack'] = 0
    df['Size'] = 0
    df['Price'] = 0
    df['CI'] = 0

    # # df.loc[(df['Casee']>=1),'Qty']=df.loc[(df['Casee'])+(df['Bottlee'])]
    # # df['Qty']=0
    # # df['Qty']=df.where(df['Casee']>1,df['Casee']+['Bottlee'],"")
    # # df['Pack']=df['packk']
    # #df.loc[df['Casee'] >= 1, ['Pack']] = df['packk']
    df['Size'] = df['Sizee']
    df.loc[df['Casee'] >= 1, ['Pack']] = (900 / df['Size'])

    # df.loc[(df['Casee'] >= 1 & df['Size']==50 & df['Size']==70), ['Pack']] = 12

    # df['Pack'] = pd.to_numeric(df.Pack)
    df.loc[df['Casee'] >= 1, ['Qty']] = df['Casee'] + (df['Bottlee'] / df['Pack'])
    df.loc[df['Size'] >= 450, ['Pack']] = 1
    df.loc[(df['Casee'] >= 1) & (df['Size'] == 50) | (df['Size'] == 70), ['Pack']] = 12
    # df.loc[df['Casee']>=1,['Pack']]=900/df['Size']
    # df.loc[df['Casee'] >= 1, ['Pack']] = 900/df['Sizee']
    # df.loc[df['Casee'] >= 1, ['Price']] = df['Case Price']
    df.loc[df['Casee'] >= 1, ['Price']] = (df['Bottle Price'] * df['Pack'])

    df.loc[df['Casee'] <= 0, ['Qty']] = df['Bottlee']
    df.loc[df['Casee'] <= 0, ['Pack']] = 1
    # df.loc[df['Casee'] <= 0, ['Price']] = df['Bottle Price'] / df['packk']
    df.loc[df['Casee'] <= 0, ['Price']] = df['Bottle Price']

    df.Qty = df.Qty.apply(int)
    # df['Qty']=round(df['Qty'],0)

    # # df.loc[(df['Cs.']>=1),'Qty']=df.loc[(df['Cs.'])+(df['Btls.'])]
    # # df['Qty']=0
    # # df['Qty']=df.where(df['Cs.']>1,df['Cs.']+['Btls.'],"")
    # # df['Pac
    # k']=df['packk']
    # df.loc[df['Cs.'] >= 1, ['Pack']] = df['packk']
    # df.loc[df['Cs.'] >= 1, ['Qty']] = df['Cs.'] + df['Btls.'] / df['Pack']
    # # df.loc[df['Cs.']>=1,['Pack']]=df['packk']
    # df.loc[df['Cs.'] >= 1, ['Price']] = df['Price per case exc. VAT']
    #
    # df['Size'] = df['Sizee']
    # df.loc[df['Cs.'] <= 0, ['Qty']] = df['Btls.']
    # df.loc[df['Cs.'] <= 0, ['Pack']] = 1
    # df.loc[df['Cs.'] <= 0, ['Price']] = df['Price per case exc. VAT'] / df['packk']
    # df.Qty = df.Qty.apply(int)
    # # df['Qty']=round(df['Qty'],0)

    file_path = '/Users/amardip.kumar/Documents/PracticePython/CI_words.xlsx'
    # from pandas import DataFrame
    # import pandas as pd
    data = {}
    df1 = pd.read_excel(file_path)
    df_dict = df1.to_dict()
    keyword = df_dict['Keyword']
    ci = df_dict['CI']
    # print(df_dict['Keyword'])
    # print(df_dict['CI'])
    # print(ci)
    for i, j in keyword.items():
        data.update({j : ci[i]})
    # import pdb;pdb.set_trace()
    for i, j in data.items():
        # print(j)
        try:
            index_val = df[df['Condition'].str.contains(i)].index.tolist()
            # if i != 'bin soiled':
            #     continue
            
            # df.loc[(df['CI'] <= 0, ['CI']) | (df['Condition'].str.contains(i)), ['CI']]=j
           
            df.loc[(df['Condition'].str.lower().str.contains(i.lower())) ,['CI']] = j
            # df.loc[(df['Condition'].str.contains(i)),['CI']] = j
        except Exception as e:
            continue





    writer = pd.ExcelWriter(path, engine='openpyxl')
    xlsx = pd.ExcelFile(path)
    for sheet in xlsx.sheet_names:
        df1 = xlsx.parse(sheet_name=sheet, index_col=0)
        df1.to_excel(writer, sheet_name=sheet)

    # print(df.loc[:, ['Qty','Pack','Size','Price','CI']].head(10))

    # print(df.iloc[:, [16,20]])
    # print(df['sizee'])
  
    # new data frame with split value columns
    # new_df = df["Format"].str.split("x", n=1, expand=True)
    # making separate first name column from new data frame
    # df["Pack"] = new[0]
    # making separate last name column from new data frame
    # df["bt_size"] = new[1]
    # Dropping old Name columns
    # data.drop(columns=["Name"], inplace=True)
    # print(df.head(10))
    # print(df)
    # print(df[:,5,16:19])
    # print(df)
    # df.to_excel('final.xlsx')

    # TodaysDate = datetime.strftime(datetime.now().date(), ' %Y_%m_%d')
    # TodaysDate = pd.datetime.now().date()
    # excelfilename = TodaysDate +".xlsx"

    # datestring = datetime.strftime(datetime.now(), ' %d%m%Y')
    # wb.save('AllData' + datestring + '.xlsm')

    # df.to_excel(r'C:\Users\harendra.gaur\Desktop\Baj_pt\' & excelfilename, index=True)
    # df.to_excel(r'C:\Users\harendra.gaur\Desktop\Baj_pt\Wine_matcher\Jubr_' + datestring + '_Harendra.xlsx',
    #             index=False, header=False,sheet_name="Sheet2")
    # df.to_excel (r'C:\Users\harendra.gaur\Desktop\Baj_pt\Wine_matcher\Final\Jubr_'+datestring + '_Harendra.xlsx', index = True, header=True)
    # #Don't forget to add '.xlsx' at the end of the path
    # df3.to_excel(writer, sheet_name='x3', index=False)
    # df4.to_excel(writer, sheet_name='x4', index=False)
    df.to_excel(writer, sheet_name="Final", index=False, header=True)
    writer.save()
    writer.close()

    print("Process completed successfully")


Remove_blank_row()
List_processing()