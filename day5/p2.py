import numpy as np

arr = np.array([1,2,3])

arr[2] = 10

print(arr[2])
print(type(arr[2]))


arr2 = np.array([
    [1,2,3],
    [4,5,np.nan]])

print(arr2[1][1])
print(type(arr2[1][1]))

print(arr[-1])

# slicing

print(arr)