import numpy as np

a = [20, 11, 12, 10, 9]
b = [15, 16, 17, 18, 17]

a_max = np.max(a)
a_min = np.min(a)

b_max = np.max(b)
b_min = np.min(b)

cr_a = (a_max-a_min)/(a_max+a_min)
cr_b = (b_max-b_min)/(b_max+b_min)

print('C.R ของ A : ', cr_a)
print('C.R ของ B : ', cr_b)
