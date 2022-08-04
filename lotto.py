import pandas as pd

def read_csv(file_path):

    return pd.read_csv(file_path)
    pass

def all_times_stat(file_to_dict):

    #print(file_to_dict['no_1'].value_counts())
    df_clean = file_to_dict.to_dict('dict')
    del df_clean['date']
    del df_clean['lottery_id']

    #print(len(df_clean))
    #print(df_clean['no_3'])
    #print(df_clean)
    #df_clean = file_to_dict.loc[:, ~file_to_dict.columns.isin(['lottery_id', 'date'])]


def specific_date(date):
    pass

def dates_range(d_range):
    pass

def by_id(id_num):
    pass







#print(df.loc[df['date'] == '19/07/2022'])

def main():

    result_file = read_csv('lotto.csv')
    dict_r = all_times_stat(result_file)
    print(dict_r)
    #Uncheck the # in the print line in order to check that the function reads the correct file
    #print(result_file)

if __name__ == '__main__':

    main()