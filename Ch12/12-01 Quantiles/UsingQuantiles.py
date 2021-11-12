import numpy as np
import statistics

data = [15, 22, 17, 14, 25, 16, 18, 18]
arr = np.array(data)

result = statistics.quantiles(data, n=4, method='exclusive')
print(result)

