import matplotlib.pyplot as plt

x1 = [2, 8, 9, 10 ,12]
y1 = [1, 9, 12, 16, 20]

x2 = [0, 7, 11, 20, 21]
y2 = [1, 12, 15, 7, 12]

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.show()
