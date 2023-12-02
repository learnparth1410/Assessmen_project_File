# 10. Create an array of numbers between 0 and 6 with increments of 0.3 and name its “x”.
# Then on the same plot, plot x, x², x³, and x⁴. For consistency, use the following style lines
# respectively, “ro”, “bs”, “g”, and “:”. Lastly, make sure that the x-axis covers 0 to 6, while
# the y-axis spans from 0 to 125. Do not worry if you are not familiar with the style lines —
# you will recognize them as soon as you see the plot. 


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,6,0.3)
y1 = x
y2 = x**2
y3 = x**3
y4 = x**4

plt.plot(x,y1,'ro',label='x')
plt.plot(x, y2, 'bs', label='x²')
plt.plot(x,y3,'g',label = 'x³')
plt.plot(x,y4,':',label = 'x⁴')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Multiple Lines Plot')
plt.legend()
plt.axis([0, 6, 0, 125])
plt.show()