from modules.soccer_data import Data
#from modules.soccer_analysis import Analysis

import time

if __name__ == '__main__':

    start = time.time()
    data = Data(Country='All')
    data.aggregateData(Season='all')
    #data.downloadData(Season='all')
    #analysis = Analysis(csv_file=data.table_csv)
    #analysis.avgFTGoals(Location='Away', Minimum=2.5)


    print('Time:', round(time.time() - start, 5), 's')
