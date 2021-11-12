import pandas as pd
 
df = pd.DataFrame({'x': [100, 200, 250], 'y': [3, 2, 4]})
result = (df['x']*df['y']).sum() / df['y'].sum()

print(result)