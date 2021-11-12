from numpy import mean, absolute

a = [20, 11, 12, 10, 9]
b = [15, 16, 17, 18, 17]

mean_a = mean(a)
md_a = mean(absolute(a - mean(a)))
cv_a = md_a/mean_a

mean_b = mean(b)
md_b = mean(absolute(b - mean(b)))
cv_b = md_b/mean_b

print('ค่าเฉลี่ย A : ', mean_a)
print('ส่วนเบี่ยงเบนเฉลี่ย A : ', md_a)
print('สัมประสิทธิ์ส่วนเบี่ยงเบนเฉลี่ย A : ', cv_a)
print('---------------------------------------')
print('ค่าเฉลี่ย B : ', mean_b)
print('ส่วนเบี่ยงเบนเฉลี่ย B : ', md_b)
print('สัมประสิทธิ์ส่วนเบี่ยงเบนเฉลี่ย B : ', cv_b)


