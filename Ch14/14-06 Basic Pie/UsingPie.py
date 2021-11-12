import matplotlib.pyplot as plt
import numpy as np

data = np.array([200, 140, 30, 75, 160])
data_label = ['A', 'B', 'C', 'D', 'E']
plt.pie(data, labels = data_label)
plt.show()
