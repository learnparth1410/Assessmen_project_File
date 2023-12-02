# C. Studying distributions of variables using histograms & bar charts to

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

sns.histplot(data[:,2], bins=30, kde=True,color = 'skyblue')
plt.title('Histogram for Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()