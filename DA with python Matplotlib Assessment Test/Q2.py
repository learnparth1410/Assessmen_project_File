# B. Visualizing relationships between two or more variables using scatter plots 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

sns.satterplot(x=data[:, 0],y=data[:, 1],hue=target,palette='viridis')
plt.title('Scatter Plot for Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()