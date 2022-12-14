import pandas as pd
from collections import OrderedDict
import csv
import webbrowser
import random

def read_csv(file_path):

    return pd.read_csv(file_path)

    pass

def power_all_times(file_to_dict):

    dict_power = {}
    p_list = file_to_dict['power_no'].values.tolist()
    for item in p_list:
        if item in dict_power:
            dict_power[item] += 1
        else:
            dict_power[item] = 1

    sorted_power = dict(sorted(dict_power.items(), key=lambda item: item[1], reverse=True))
    return sorted_power



def all_times_stat(file_to_dict):

    dict_r = {}
    lists = file_to_dict.values.tolist()
    for list_item in lists:
        list_item.pop(0)
        list_item.pop(0)
        list_item.pop(6)
        for l in list_item:
            if l in dict_r:
                dict_r[l] += 1
            else:
                dict_r[l] = 1

    sorted_dict = dict(sorted(dict_r.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict



def specific_date(date):
    pass

def dates_range(d_range):
    pass

def by_id(id_num):

    pass

def statistics(data, power):

    stat_num = []
    for key, value in data.items():
        if value >= 5:
            stat_num.append(key)

    stat_power = []
    for key, value in power.items():
        if value >= 4:
            stat_power.append(key)



    nlist = []
    #for n in range(len(stat_num)):
    nlist.append(random.sample(stat_num, 6))
    print(f'The numbers are: {nlist}')


    plist = []
    plist.append(random.sample(stat_power, 1))
    print(f'The power number is: {plist}')







def print_data(data, power, num):

    if num == 1:
        print('Printing most LUCKY numbers in descending order:\n==================================================\n')
        df = pd.DataFrame(data.items(), columns=['Number', 'Times'])
        print(df.to_string(index=False))
        print(df.to_html('power.html', index=False, justify='center'))

        print('\nPrinting the most LUCKY power numbers in descending order:\n===========================================================\n')
        df = pd.DataFrame(power.items(), columns=['Power Number', 'Times'])
        #print(df.to_string(index=False))
        #print(df.to_html('power.html', index=False, justify='center'))
        with open('power.html', 'a') as fhtml:
            fhtml.write(df.to_html(index=False, justify='center'))

    webbrowser.open_new_tab('power.html')



#print(df.loc[df['date'] == '19/07/2022'])

def main():

    result_file = read_csv('lotto.csv')
    dict_r = all_times_stat(result_file)
    dict_power = power_all_times(result_file)
    #print_data(dict_r, dict_power, 1)
    statistics(dict_r, dict_power)


    #Uncheck the # in the print line in order to check that the function reads the correct file
    #print(result_file)

if __name__ == '__main__':

    main()