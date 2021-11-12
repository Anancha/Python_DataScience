import numpy as np

a = [20, 11, 12, 10, 9]
b = [15, 16, 17, 18, 17]

q1_a = np.quantile(a, 0.25, interpolation='linear')
q3_a = np.quantile(a, 0.75, interpolation='linear')

q1_b = np.quantile(b, 0.25, interpolation='linear')
q3_b = np.quantile(b, 0.75, interpolation='linear')

cq_a = (q3_a-q1_a)/(q3_a+q1_a)
cq_b = (q3_b-q1_b)/(q3_b+q1_b)

print('Q1 ของ A : ', q1_a)
print('Q3 ของ A : ', q3_a)
print('C.Q ของ A : ', cq_a)
print('---------------------------------------')
print('Q1 ของ B : ', q1_b)
print('Q3 ของ B : ', q3_b)
print('C.Q ของ B : ', cq_b)
