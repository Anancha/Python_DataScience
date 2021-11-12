import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4, 5, 6, 8, 10, 11, 12]
y1 = [2, 4, 6, 8, 9, 10, 12, 13, 14, 15]

x2 = [0, 4, 8, 11, 12, 14, 15, 16, 17, 18]
y2 = [2, 5, 6, 12, 13, 14, 16, 18, 20, 21]

colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

plt.scatter(x1, y1, c=colors, s=350)
plt.scatter(x2, y2, c=colors, s=1000, alpha=0.5)
plt.show()
