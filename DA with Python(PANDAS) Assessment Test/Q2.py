# 2. Creating A Pandas Data Frame and Using Sample Data Sets 
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
       }

df = pd.DataFrame(data)
print(df)