# D. Visualizing two-dimensional data using heatmaps 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  # Import Pandas
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

# Convert the NumPy array to a Pandas DataFrame
df = pd.DataFrame(data, columns=iris.feature_names)

# Heatmap using Seaborn
correlation_matrix = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Feature Correlation')
plt.show()
