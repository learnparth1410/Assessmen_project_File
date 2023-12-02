import pandas as pd

df_csv = pd.read_csv('your_File.csv')

summary_statistics = df_csv.describe()
print(summary_statistics)