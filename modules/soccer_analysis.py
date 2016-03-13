import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.width = 300
pd.options.display.max_rows = 50
pd.options.display.precision = 2

class Analysis():

    def __init__(self, csv_file):

        self.table = pd.read_csv(csv_file)
        #self.table.info()
        pass

    def avgFTGoals(self, Location = 'Home', Minimum = 2):

        if Location == 'Home':
            loc = 'HomeTeam'
        else:
            loc = 'AwayTeam'

        ptable = self.table.pivot_table(values=['FTHG', 'FTAG' ], columns=['League', loc], aggfunc='mean', fill_value=0)
        ptable.sort()
        print(ptable[ptable.values > 1])
        ptable[ptable.values > Minimum ].head(75).plot(kind='barh', title='FT Home Goals', grid=True, fontsize=10)
        plt.show()
        ptable.plot(kind="scatter", x="FTHG", y="FTAG")
        print(self.table.describe())
        print(self.table[['Country', 'League', 'Date', 'HomeTeam', 'AwayTeam', 'FTR', 'FTHG','FTAG',
                          'BbAv>2.5', 'BbAv<2.5',
                          ]][self.table['FTHG' ] + self.table['FTAG'] > 2])