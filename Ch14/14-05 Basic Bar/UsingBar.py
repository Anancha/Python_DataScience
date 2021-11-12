import matplotlib.pyplot as plt
import numpy as np

name = np.array(["AAA", "BBB", "CCC"])
data = np.array([110, 140, 80])

colors = np.array(['red', 'blue', 'green'])
plt.barh(name, data, color=colors)
plt.show()
