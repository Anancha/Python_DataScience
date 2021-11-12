from numpy import mean, absolute

data = [10, 15, 16, 20, 17]

result = mean(absolute(data - mean(data)))
print(result)