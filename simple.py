import pandas as pd
import numpy as np
def ge(data,x):
    ans = []
    temp = data[x].isnull()
    print data[x].isnull().sum()
    for i in range(0,len(temp)):
        if(temp[i]):
            ans.append(i)
    return ans

data_train = pd.read_csv('Data_Test.csv')
l = data_train.columns
print l
for j in data_train.columns:
    if(j != 'New_Price'):
        print j,ge(data_train,j)

