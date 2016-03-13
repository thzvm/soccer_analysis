import pandas as pd
data = pd.read_csv('data/All_Seasons.csv', error_bad_lines=False)
data.info()
print(data.describe())