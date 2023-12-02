'''
Question 1. Plotting graph For IRIS Dataset Using Seaborn Library And
matplotlib.pyplot library 
'''

# A. Creating and customizing line charts using Matplotlib

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target

plt.plot(data[:, 0], label='Sepal Length')
plt.plot(data[:, 1], label='Sepal Width')
plt.plot(data[:, 2], label='Petal Length')
plt.plot(data[:, 3], label='Petal Width')

plt.title('Line Chart for Iris Dataset')
plt.xlabel('Samples')
plt.ylabel('Feature Values')
plt.legend()
plt.show()