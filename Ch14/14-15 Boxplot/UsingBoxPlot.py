import matplotlib.pylab as plt
import numpy as np

data = [42, 40, 45, 48, 63, 60]
fig = plt.figure(1, figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(data, vert=False, manage_ticks=True)
ax.set_xlabel('Values')
ax.set_yticklabels(['Products'])

q = np.quantile(data, [0.00, 0.25, 0.50, 0.75, 1.00])
ax.vlines(q, ymin=0, ymax=100, color='red', ls=':')

ax.set_xticks(q)
ax.set_ylim(0.5, 1.5)
plt.show()
