# 1. Compute the minimum, 25th percentile, median, 75th, and maximum of ser.

import numpy as np 
import pandas as pd

ser = pd.Series(np.random.random(1000))

min_Value = ser.min()

q25 = ser.quantile(0.25)

median_Value = ser.median()

q75 = ser.quantile(0.75)

max_Value = ser.max()


print(f"Minimum: {min_Value}")
print(f"25th Percentile: {q25}")
print(f"Median: {median_Value}")
print(f"75th Percentile: {q75}")
print(f"Maximum: {max_Value}")