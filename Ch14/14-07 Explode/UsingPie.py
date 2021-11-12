import matplotlib.pyplot as plt
import numpy as np

data = np.array([200, 140, 30, 75, 160])
data_label = ['A', 'B', 'C', 'D', 'E']
data_explode = [0.3, 0, 0.2, 0, 0]

plt.pie(data, labels = data_label, explode=data_explode)
plt.legend()
plt.show()
