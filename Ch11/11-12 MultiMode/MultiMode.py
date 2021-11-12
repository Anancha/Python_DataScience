import numpy as np
import statistics as st

data = [22, 17, 14, 14, 19, 18, 17, 22, 10, 11]
arr = np.array(data)

single_mode = st.mode(arr)
multi_mode = st.multimode(arr)

print('ฐานนิยมแบบ 1 ค่า : ', single_mode)
print('ฐานนิยมแบบหลายค่า : ', multi_mode)
