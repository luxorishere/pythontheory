import random
import pandas as pd

d = {}
for i in range(1,4):
    d[i] = {j: random.randint(1,100) for j in range(1,4)}
    
df = pd.DataFrame(d)
print(df)

print(df.describe())