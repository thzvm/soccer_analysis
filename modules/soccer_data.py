import pandas as pd
import time
import csv
from urllib.request import urlopen

SITE = 'http://www.football-data.co.uk/mmz4281/'

Country = [['GBR', 'England', ['E0', 'E1', 'E2', 'E3'],
            {'E0': 'Premier League','E1': 'Championship','E2': 'League 1','E3': 'League 2'}],
           ['SCT', 'Scotland', ['SC0', 'SC1', 'SC2', 'SC3'],
            {'SC0': 'Premier League', 'SC1': 'Division 1', 'SC2': 'Division 2', 'SC3': 'Division 3'}],
           ['DEU', 'Germany', ['D1', 'D2'],
            {'D1': 'Bundesliga 1', 'D2': 'Bundesliga 2'}],
           ['ITA', 'Italy', ['I1', 'I2'],
            {'I1': 'Serie A', 'I2': 'Serie B'}],
           ['ESP', 'Spain', ['SP1', 'SP2'] ,
            {'SP1': 'La Liga Primera Division', 'SP2': 'La Liga Segunda Division'}],
           ['FRA', 'France', ['F1', 'F2'],
            {'F1': 'Le Championnat', 'F2': 'Division 2'}],
           ['NLD', 'Netherlands', ['N1'],
            {'N1': 'Eredivisie'}],
           ['BEL', 'Belgium', ['B1'],
            {'B1': 'Jupiler League'}],
           ['PRT', 'Portugal', ['P1'],
            {'P1': 'Liga I'}],
           ['TUR', 'Turkey', ['T1'],
            {'T1': 'Futbol Ligi 1'}],
           ['GRC', 'Greece', ['G1'],
            {'G1': 'Ethniki Katigoria'}]]

Years = ['9394', '9495', '9596', '9697', '9798', '9899', '9900', '0001',
          '0102', '0203', '0304', '0405', '0506', '0607', '0708', '0809',
          '0910', '1011', '1112', '1213', '1314', '1415', '1516', '1617']

def restructuring(link, filename):

    csv_file = link
    return_file = 'temp/' + filename
    try:
        response = urlopen(csv_file)
        head = response.readline().decode("utf-8").replace('\r\n', '').split(',')
        with open(return_file, 'w', newline='') as csvout:

            spamwriter = csv.writer(csvout, delimiter=',')
            spamwriter.writerow(head)
            for row in response:

                if len(row.decode("utf-8").split(',')) == len(head):
                    spamwriter.writerow(row.decode("utf-8").replace('\r\n', '').split(','))
                elif len(row.decode("utf-8").split(',')) > len(head):
                    spamwriter.writerow(row.decode("utf-8").replace('\r\n', '').split(',')[:len(head)])

    except Exception as e:
        print(link)
        print(return_file)
        return_file = None
        print('FAAAAAAAIL', e)


    return return_file


class Data():
    """http://www.football-data.co.uk/data.php"""

    def __init__(self, Country, League='1', Season='15/16'):

        if Country == 'All':
            self.country = 'All'
            self.league = League
            self.season = Season
            #self.downloadData()
            #self.aggregateData()
        else:
            self.country = Country
            self.league = League

    def downloadData(self, Season='15/16'):

        if Season == 'all':
            for i in range(len(Country)):
                for k in range(len(Country[i][2])):
                    for y in Years:
                        query = SITE + y + '/' + Country[i][2][k] + '.csv'
                        filename = 'data/' + y + '_' + Country[i][1] + \
                                       '_' + Country[i][3][Country[i][2][k]].replace(' ', '_') + '.csv'
                        try:
                            data = pd.read_csv(query)
                            data.drop('Div', axis=1, inplace=True)
                            data.insert(loc=0, column='Country', value=Country[i][1])
                            data.insert(loc=1, column='League', value=Country[i][3][Country[i][2][k]])
                            data.to_csv(filename, header=True, index=None, mode='a')
                            time.sleep(0)
                        except Exception as e:
                            try:

                                data = pd.read_csv(restructuring(link=query, filename=filename))
                                data.drop('Div', axis=1, inplace=True)
                                data.insert(loc=0, column='Country', value=Country[i][1])
                                data.insert(loc=1, column='League', value=Country[i][3][Country[i][2][k]])
                                data.to_csv(filename, header=True, index=None, mode='a')
                                time.sleep(0)

                            except:
                                print(str(e).replace('\n', ''), ',', y, ',', Country[i][1], ',', Country[i][3][Country[i][2][k]], ',', query )
                                etxt = open('error.txt', mode='a')
                                etxt.write(str(e).replace('\n', '') + ';' + y + ';' + Country[i][1] + ';' +
                                       Country[i][3][Country[i][2][k]]+  ';' + query + '\n')
                                etxt.close()


        else:

            for i in range(len(Country)):
                for k in range(len(Country[i][2])):
                    query = SITE + Season.replace('/', '') + '/'+ Country[i][2][k] + '.csv'
                    filename = 'data2/'+ Season.replace('/', '') + '_' + Country[i][1] + \
                               '_' + Country[i][3][Country[i][2][k]].replace(' ', '_') + '.csv'
                    data = pd.read_csv(query)
                    data.drop('Div', axis=1, inplace=True)
                    data.insert(loc=0, column='Country', value=Country[i][1])
                    data.insert(loc=1, column='League', value=Country[i][3][Country[i][2][k]])
                    data.to_csv(filename, header=True, index=None, mode='a')
                    time.sleep(1)

    def aggregateData(self, Season='15/16'):

        if Season == 'all':
            table_array = []
            for i in range(len(Country)):
                for k in range(len(Country[i][2])):
                    for y in Years:
                        try:

                            filequery = 'data/' + y + '_' + Country[i][1] + \
                                        '_' + Country[i][3][Country[i][2][k]].replace(' ', '_') + '.csv'

                            temp_table = pd.read_csv(filequery, error_bad_lines=False)
                            try:
                                temp_table.drop('B365A', axis=1, inplace=True)
                                temp_table.drop('B365D', axis=1, inplace=True)
                                temp_table.drop('B365H', axis=1, inplace=True)
                                temp_table.drop('BWA', axis=1, inplace=True)
                                temp_table.drop('BWD', axis=1, inplace=True)
                                temp_table.drop('BWH', axis=1, inplace=True)
                                temp_table.drop('IWA', axis=1, inplace=True)
                                temp_table.drop('IWD', axis=1, inplace=True)
                                temp_table.drop('IWH', axis=1, inplace=True)
                                temp_table.drop('LBA', axis=1, inplace=True)
                                temp_table.drop('LBD', axis=1, inplace=True)
                                temp_table.drop('LBH', axis=1, inplace=True)
                                temp_table.drop('PSA', axis=1, inplace=True)
                                temp_table.drop('PSD', axis=1, inplace=True)
                                temp_table.drop('PSH', axis=1, inplace=True)
                                temp_table.drop('VCA', axis=1, inplace=True)
                                temp_table.drop('VCD', axis=1, inplace=True)
                                temp_table.drop('VCH', axis=1, inplace=True)
                                temp_table.drop('WHA', axis=1, inplace=True)
                                temp_table.drop('WHD', axis=1, inplace=True)
                                temp_table.drop('WHH', axis=1, inplace=True)
                                table_array.append(temp_table)
                            except: table_array.append(temp_table)

                            frames = [files for files in table_array]

                            self.table = pd.concat(frames, join='outer')

                            sort = ['Country', 'League', 'Date', 'HomeTeam', 'AwayTeam', 'HTHG', 'HTAG', 'HTR', 'FTHG',
                                    'FTAG', 'FTR',
                                    'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR',
                                    'Bb1X2', 'BbMxH', 'BbAvH', 'BbMxD', 'BbAvD', 'BbMxA', 'BbAvA', 'BbOU', 'BbMx>2.5',
                                    'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 'BbMxAHH', 'BbAvAHH',
                                    'BbMxAHA', 'BbAvAHA']

                            self.table = self.table[sort]
                            self.table_csv = 'data/All_Seasons.csv'
                            self.table.to_csv(self.table_csv, header=True, index=None, mode='w')
                            time.sleep(1)
                        except Exception as e:
                            print(e)
                            print(y, Country[i][1], Country[i][3][Country[i][2][k]])
                            print(filequery)
                            print('___________________________')

        else:

            table_array = []

            for i in range(len(Country)):
                for k in range(len(Country[i][2])):
                    filequery = 'data/' + Season.replace('/', '') + '_' + Country[i][1] + \
                                '_' + Country[i][3][Country[i][2][k]].replace(' ', '_') + '.csv'
                    temp_table = pd.read_csv(filequery)
                    temp_table.drop('Div', axis=1, inplace=True)
                    temp_table.insert(loc=0, column='Country', value=Country[i][1])
                    temp_table.insert(loc=1, column='League', value=Country[i][3][Country[i][2][k]])
                    temp_table.drop('B365A', axis=1, inplace=True)
                    temp_table.drop('B365D', axis=1, inplace=True)
                    temp_table.drop('B365H', axis=1, inplace=True)
                    temp_table.drop('BWA', axis=1, inplace=True)
                    temp_table.drop('BWD', axis=1, inplace=True)
                    temp_table.drop('BWH', axis=1, inplace=True)
                    temp_table.drop('IWA', axis=1, inplace=True)
                    temp_table.drop('IWD', axis=1, inplace=True)
                    temp_table.drop('IWH', axis=1, inplace=True)
                    temp_table.drop('LBA', axis=1, inplace=True)
                    temp_table.drop('LBD', axis=1, inplace=True)
                    temp_table.drop('LBH', axis=1, inplace=True)
                    temp_table.drop('PSA', axis=1, inplace=True)
                    temp_table.drop('PSD', axis=1, inplace=True)
                    temp_table.drop('PSH', axis=1, inplace=True)
                    temp_table.drop('VCA', axis=1, inplace=True)
                    temp_table.drop('VCD', axis=1, inplace=True)
                    temp_table.drop('VCH', axis=1, inplace=True)
                    temp_table.drop('WHA', axis=1, inplace=True)
                    temp_table.drop('WHD', axis=1, inplace=True)
                    temp_table.drop('WHH', axis=1, inplace=True)
                    table_array.append(temp_table)

            frames = [files for files in table_array]
            self.table = pd.concat(frames, join='outer')
            sort = ['Country', 'League', 'Date', 'HomeTeam', 'AwayTeam', 'HTHG', 'HTAG', 'HTR', 'FTHG', 'FTAG', 'FTR',
                    'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR',
                    'Bb1X2', 'BbMxH', 'BbAvH', 'BbMxD', 'BbAvD', 'BbMxA', 'BbAvA', 'BbOU', 'BbMx>2.5',
                    'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 'BbMxAHH', 'BbAvAHH', 'BbMxAHA', 'BbAvAHA']
            self.table = self.table[sort]
            self.table_csv = 'data/1516.csv'
            self.table.to_csv(self.table_csv, header=True, index=None, mode='w')
