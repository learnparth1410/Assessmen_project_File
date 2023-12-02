'''
12. Plot a histogram of x, where x consists of 100,000 randomly-selected points with a normal
distribution (hint: you can use numpy.random.randn() to generate the random points). The
histogram should have 10 bins. Look at how the histogram changes when we try 20 and 50
bins. 
'''

import numpy as np
import matplotlib.pyplot as plt

# Generate 100,000 random points with a normal distribution
x = np.random.randn(100000)

# Plot histogram with 10 bins
plt.hist(x, bins=10, color='blue', alpha=0.7, label='10 Bins')

# Plot histogram with 20 bins
plt.hist(x, bins=20, color='green', alpha=0.7, label='20 Bins')

# Plot histogram with 50 bins
plt.hist(x, bins=50, color='red', alpha=0.7, label='50 Bins')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Different Bins')
plt.legend()
plt.show()
