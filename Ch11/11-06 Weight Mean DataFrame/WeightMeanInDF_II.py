import pandas as pd
import numpy as np
 
df = pd.DataFrame({'x': [100, 200, 250], 'y': [3, 2, 4]})
result = np.average(df['x'], weights=df['y'])

print(result)