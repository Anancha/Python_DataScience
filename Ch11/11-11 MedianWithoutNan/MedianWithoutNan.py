import numpy as np

data = [22, 17, 14, np.nan]
arr = np.array(data)

normal_median = np.median(arr)
clean_median = np.nanmedian(arr)
print('ค่ามัธยฐานปกติ : ', normal_median)
print('ค่ามัธยฐานตัดค่า Miss Value : ', clean_median)

