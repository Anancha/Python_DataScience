import numpy as np

a = [20, 11, 12, 10, 9]
b = [15, 16, 17, 18, 17]

a_sd = np.std(a)
a_mean = np.mean(a)

b_sd = np.std(b)
b_mean = np.mean(b)

cv_a = a_sd/a_mean
cv_b = b_sd/b_mean

print('ค่าเฉลี่ยเลขคณิต A : ', a_mean)
print('ค่าเฉลี่ยเลขคณิต B : ', b_mean)
print('ส่วนเบี่ยงเบนมาตรฐาน A : ', a_sd)
print('ส่วนเบี่ยงเบนมาตรฐาน B : ', b_sd)
print('C.V ของ A : ', cv_a)
print('C.V ของ B : ', cv_b)

