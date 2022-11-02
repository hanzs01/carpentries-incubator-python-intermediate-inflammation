import numpy as np 
# from models import daily_mean 

data = np.loadtxt(fname='data\inflammation-01.csv', delimiter=',')
print(data.shape)

from inflammation.models import daily_mean
daily_mean (
    [
        [1 , 2],
        [3 , 4],
        [5 , 6] 
    ]
)

# daily_mean(data[0:4])
