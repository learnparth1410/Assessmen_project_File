import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

# Load the digits dataset (you can replace this with your own image data)
digits = load_digits()
images = digits.images
# Assuming 'image' is your image data
plt.imshow(image[0], cmap='gray')
plt.title('Displayed Image')
plt.show()
