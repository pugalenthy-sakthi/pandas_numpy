import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# arr = np.array([1,2,3,4,5],ndmin=10)
# print(arr)

arr1 = np.array([1,2,3,4],ndmin=2)

print('array shape',arr1.shape)


""" 
the main diffrence between the numpy's array vs normal python lists is the list are stored int the random memory locations and the the locations of the list element are stored in the hash map that is works as a map locator
But in the numpy the array are same datatype and the element are stored in continues memeory locations so the accessing the element is much faster compared to the python list
"""

print(arr1[0,1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
print(arr[::2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
print(arr[0:4,2])

print(arr[0:2, 1:4])


arr1 = np.array([1,2,3,4,5])

arr2 = arr1.copy()

print(arr1,arr2)
arr1[2] = 100
print(arr1,arr2)

arr1 = np.array([1,2,3,4,5])

arr2 = arr1.view()

print(arr1,arr2)
arr1[2] = 100
print(arr1,arr2)



arr1 = np.array([1,2,3,4,5])

arr2 = arr1.view()

print(arr1,arr2)
arr2[2] = 100
print(arr1,arr2)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print("reshaped_Array\n",newarr)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
  
  
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2))

print("vertical statck",arr)


print('Splitting Array')

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print("Splitting 2d array")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

newarr = np.array_split(arr, 3)

print(newarr)

print("Array Search")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x[0])