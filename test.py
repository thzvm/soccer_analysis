import pandas as pd
import seaborn
import csv
import matplotlib.pyplot as plt
import numpy as np
#data_file = 'UKPL.csv'
#data_file = 'data/1516_England_Premier_League.csv'
data_file = 'data/_1516_data.csv'

data_head = 'data/_HEAD.csv'
head_dict = {}
head = []
pandas_file = 'pandas.csv'
with open(data_head) as file:
    for items in file:
        data = items.split(',')
        head_dict[data[0]] = data[1].replace('\n', '')

with open(data_file) as file:
    head_line = file.readline().split(',')
    for item in head_line:
        head.append(head_dict[item.replace('\n', '')])

pd.options.display.width = 200
pd.options.display.max_rows = 10000
pd.options.display.precision = 2
data = pd.read_csv(data_file, delimiter=',')
data.columns = head
#data.info()
print(len(data.columns))
for column in data.columns:
    print(column)

if len(data.columns) < 50:

    data.insert(loc=12, column='Match Referee', value='None')
    data.insert(loc=13, column='Shots (Home)', value=0)
    data.insert(loc=14, column='Shots (Away)', value=0)
    data.insert(loc=15, column='Shots on Target (Home)', value=0)
    data.insert(loc=16, column='Shots on Target (Away)', value=0)
    data.insert(loc=17, column='Fouls (Home)', value=0)
    data.insert(loc=18, column='Fouls (Away)', value=0)
    data.insert(loc=19, column='Corners (Home)', value=0)
    data.insert(loc=20, column='Corners (Away)', value=0)
    data.insert(loc=21, column='Yellow Cards (Home)', value=0)
    data.insert(loc=22, column='Yellow Cards (Away)', value=0)
    data.insert(loc=23, column='Red Cards (Home)', value=0)
    data.insert(loc=24, column='Red Cards (Away)', value=0)

if len(data.columns) < 63:
    data.insert(loc=63, column='BbAvAHA', value=0)

data.info()
'''
stats = data[['Data','Home', 'Away', 'FT Result', 'FT Away Goals', 'FT Away Goals']][data['FT Away Goals'] > 1]
#stats.head(30).plot(kind='bar')
#plt.show()
ptable = data.pivot_table(values='FT Home Goals', columns=['League', 'Away'], aggfunc='mean', fill_value = 0)
ptable.sort()
print(ptable[ptable.values > 1])
ptable[ptable.values > 2.2].head(75).plot(kind='barh', title='FT Home Goals', grid=True, legend=None, fontsize=10)
plt.show()'''
