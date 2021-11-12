import statistics as st

data = [12, 16, 17, 19, 20, 20]
result = st.median(data)
result_low = st.median_low(data)
result_high = st.median_high(data)

print('ปกติ : ', result)
print('low : ', result_low)
print('high : ', result_high)

