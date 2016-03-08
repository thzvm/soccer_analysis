import pandas as pd
import time

SITE = 'http://www.football-data.co.uk/mmz4281/'

Country = [['GBR', 'England', ['E0', 'E1', 'E2', 'E3'], {'E0': 'Premier League','E1': 'Championship','E2': 'League 1','E3': 'League 2'}],
           ['SCT', 'Scotland', ['SC0', 'SC1', 'SC2', 'SC3'], {'SC0': 'Premier League', 'SC1': 'Division 1', 'SC2': 'Division 2', 'SC3': 'Division 3'}],
           ['DEU', 'Germany', ['D1', 'D2'], {'D1': 'Bundesliga 1', 'D2': 'Bundesliga 2'}],
           ['ITA', 'Italy', ['I1', 'I2'], {'I1': 'Serie A', 'I2': 'Serie B'}],
           ['ESP', 'Spain', ['SP1', 'SP2'] , {'SP1': 'La Liga Primera Division', 'SP2': 'La Liga Segunda Division'}],
           ['FRA', 'France', ['F1', 'F2'], {'F1': 'Le Championnat', 'F2': 'Division 2'}],
           ['NLD', 'Netherlands', ['N1'], {'N1': 'Eredivisie'}],
           ['BEL', 'Belgium', ['B1'], {'B1': 'Jupiler League'}],
           ['PRT', 'Portugal', ['P1'], {'P1': 'Liga I'}],
           ['TUR', 'Turkey', ['T1'], {'T1': 'Futbol Ligi 1'}],
           ['GRC', 'Greece', ['G1'], {'G1': 'Ethniki Katigoria'}]]

class Data():
    """http://www.football-data.co.uk/data.php"""

    def __init__(self, Country, League='1', Season='15/16'):

        if Country == 'All':
            self.country = 'All'
            self.league = League
            self.season = Season
            self.getAllData()
        else:
            self.country = Country
            self.league = League

    def getAllData(self, Season='15/16'):

        header = False

        for i in range(len(Country)):
            for k in range(len(Country[i][2])):
                query = SITE + Season.replace('/', '') + '/'+ Country[i][2][k] + '.csv'
                filequery = 'data/'+ Season.replace('/', '') + '_' + Country[i][1] + \
                           '_' + Country[i][3][Country[i][2][k]].replace(' ', '_') + '.csv'
                print(query)
                filename = 'data/_1516_data.csv'
                #print(filename)
                data = pd.read_csv(filequery)
                old_len = len(data.columns)
                data.drop('Div', axis=1, inplace=True)
                data.insert(loc=0, column='Country', value=Country[i][1])
                data.insert(loc=1, column='Div', value=Country[i][3][Country[i][2][k]])
                if len(data.columns) < 55:
                    data.insert(loc=11, column='Match Referee', value='None')
                    data.insert(loc=12, column='Shots (Home)', value=0)
                    data.insert(loc=13, column='Shots (Away)', value=0)
                    data.insert(loc=14, column='Shots on Target (Home)', value=0)
                    data.insert(loc=15, column='Shots on Target (Away)', value=0)
                    data.insert(loc=16, column='Fouls (Home)', value=0)
                    data.insert(loc=17, column='Fouls (Away)', value=0)
                    data.insert(loc=18, column='Corners (Home)', value=0)
                    data.insert(loc=19, column='Corners (Away)', value=0)
                    data.insert(loc=20, column='Yellow Cards (Home)', value=0)
                    data.insert(loc=21, column='Yellow Cards (Away)', value=0)
                    data.insert(loc=22, column='Red Cards (Home)', value=0)
                    data.insert(loc=23, column='Red Cards (Away)', value=0)

                #if len(data.columns) < 63:
                    #data.insert(loc=63, column='BbAvAHA', value=0)

                new_len = len(data.columns)
                print(old_len, new_len)
                if header == False:
                    data.to_csv(filename, header=True, index=None, mode='a')
                    header = True
                else:
                    data.to_csv(filename, header=False, index=None, mode='a')

                #time.sleep(3)
                pass
