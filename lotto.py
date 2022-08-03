import pandas as pd

def read_csv(file_path):

    return pd.read_csv(file_path)
    pass

def all_times_stat():

    pass

def specific_date(date):
    pass

def dates_range(d_range):
    pass

def by_id(id_num):
    pass







#print(df.loc[df['date'] == '19/07/2022'])

def main():

    result_file = read_csv('lotto.csv')
    #Uncheck the # in the print line in order to check that the function reads the correct file
    #print(result_file)

if __name__ == '__main__':

    main()