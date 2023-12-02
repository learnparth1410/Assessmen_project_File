# 3. Using NumPy, create a Pandas Data Frame with five rows and three columns. 
import numpy as np
import pandas as pd

np_data = np.random.rand(5,3)
df_np = pd.DataFrame(np_data,Columns = ['Column1','Column2','Column3'])
print(df_np)