# numpy 

import numpy as np 
import pandas as pd 

arr1 = np.array([1,2,3,4])
arr2 = np.zeros((2,3))
arr3 = np.random.rand(2,3)
print(arr1)
print(arr2)
print(arr3)


series1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("series1:\n", series1)

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 28, 35],
    'city': ['New York', 'London', 'Tokyo', 'Paris'],
    'salary': [50000, 60000, 55000, 70000]
}
df = pd.DataFrame(data)
print("df:\n", df)