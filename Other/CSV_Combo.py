import pandas as pd

# reading csv files
data1 = pd.read_csv('datasets/Zoho Export - Borrowers.csv')
data2 = pd.read_csv('datasets/Zoho Export - Deals.csv')
  
# using merge function by setting how='outer'
output4 = pd.merge(data1, data2, 
                   on='Borrower ID', 
                   how='outer')

output4.to_csv('D:/Work/Code/python-pipedrive/datasets/Merged_Data.csv',index=False)