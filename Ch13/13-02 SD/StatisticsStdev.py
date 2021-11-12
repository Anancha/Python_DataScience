import numpy as np
import statistics as st

data = [120, 124, 130, 115]
arr = np.array(data)

sd = st.stdev(arr)
print('ส่วนเบี่ยงเบนมาตรฐาน : ', sd)

