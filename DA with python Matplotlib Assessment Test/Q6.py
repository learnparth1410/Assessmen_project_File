# F. Plotting multiple Matplotlib and Seaborn charts in a grid

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  # Import Pandas
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

# Corrected function name from plt.subplot() to plt.subplots()
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Scatter plot
sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=target, palette='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Scatter Plot for Sepal Length vs Sepal Width')

# Histogram
sns.histplot(data[:, 2], bins=30, kde=True, color='skyblue', ax=axes[0, 1])
axes[0, 1].set_title('Histogram for Petal Length')

# Heatmap
sns.heatmap(pd.DataFrame(data).corr(), annot=True, cmap='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Heatmap of Feature Correlation')

# Line chart
axes[1, 1].plot(data[:, 0], label='Sepal Length')
axes[1, 1].plot(data[:, 1], label='Sepal Width')
axes[1, 1].plot(data[:, 2], label='Petal Length')
axes[1, 1].plot(data[:, 3], label='Petal Width')
axes[1, 1].set_title('Line Chart for Iris Dataset')
axes[1, 1].legend()

plt.tight_layout()
plt.show()
