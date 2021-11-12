import numpy as np

data = [12,4,10,10,15,13,16,10,5,25,7,3]
o = np.sort(data)
q1 = np.percentile(data, 25, interpolation = 'lower')
q3 = np.percentile(data, 75, interpolation = 'lower')
iqr = q3-q1
qd = iqr / 2

print(o)
print('Q1 :', q1)
print('Q3 :', q3)
print('IQR : ', iqr)
print('Q.D : ', qd)

