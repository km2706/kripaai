import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[1:4])
print(arr[3:])
print(arr[:4])

print(arr[-3:-1])
print(arr[-3:])
print(arr[:-1])

"""
1,2,3,4
0,1,2,3
[-4,-3,-2,-1]
"""