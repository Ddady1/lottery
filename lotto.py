import pandas as pd
from collections import OrderedDict
import csv

def read_csv(file_path):

    return pd.read_csv(file_path)

    pass

def all_times_stat(file_to_dict):

    dict_r = {}
    lists = file_to_dict.values.tolist()
    for list_item in lists:
        list_item.pop(0)
        list_item.pop(0)
        for l in list_item:
            if l in dict_r:
                dict_r[l] += 1
            else:
                dict_r[l] = 1

    #dict_r = OrderedDict(sorted(dict_r.items()))

    sorted_dict = dict(sorted(dict_r.items(), key=lambda item: item[1], reverse=True))

    #print(dict_r)
    return sorted_dict



def specific_date(date):
    pass

def dates_range(d_range):
    pass

def by_id(id_num):

    pass

def print_data(data, num):

    if num == 1:
        print('Printing most LUCKY numbers in descending order:\n________________________________________________\n')
        df = pd.DataFrame(data.items(), columns=['Number', 'Times'])
        print(df.to_string(index=False))








#print(df.loc[df['date'] == '19/07/2022'])

def main():

    result_file = read_csv('lotto.csv')
    dict_r = all_times_stat(result_file)
    print_data(dict_r, 1)


    #Uncheck the # in the print line in order to check that the function reads the correct file
    #print(result_file)

if __name__ == '__main__':

    main()