import pandas as pd

# reading csv files
data1 = pd.read_csv('filename')
data2 = pd.read_csv('filename')
  
# using merge function by setting how='outer'
output4 = pd.merge(data1, data2, 
                   on='columnname', 
                   how='outer')

output4.to_csv('output',index=False)
