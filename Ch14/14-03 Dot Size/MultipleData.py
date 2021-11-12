import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]

x2 = [0, 4, 8, 11]
y2 = [2, 5, 6, 12]

colors = np.array([0, 33, 66, 100])

plt.scatter(x1, y1, c=colors, s=75)
plt.scatter(x2, y2, c=colors, s=250)
plt.show()
