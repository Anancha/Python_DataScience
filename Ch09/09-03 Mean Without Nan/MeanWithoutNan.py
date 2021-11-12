import numpy as np

data = [22, 17, 14, np.nan]
arr = np.array(data)

normal_mean = np.mean(arr)
clean_mean = np.nanmean(arr)
print('ค่าเฉลี่ยเลขคณิตปกติ : ', normal_mean)
print('ค่าเฉลี่ยเลขคณิตตัดค่า Miss Value : ', clean_mean)

