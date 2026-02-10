import numpy as np

arr = np.array([1,2,3])

print(arr)
print(type(arr))
print(np.shape(arr))
print(arr.shape)


arr2 = np.array([[1,2,3],[4,5,np.nan]])

print(arr2)
print(arr2.shape)

arr3 = np.array([
    [
        [1,2,3], 
        [4,5,6]
    ], 
    [
        [7,8,9],
        [np.nan, np.nan, np.nan]
    ]])

print(arr3)
print(arr3.shape)


"""
array, shape, slice
broadcasting
vectorized operations
aggrigation functions
missing data handeling
normalizations
"""