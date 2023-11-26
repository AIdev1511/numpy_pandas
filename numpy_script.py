import numpy as np

# Creating a numpy array
# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

data = np.random.rand(2,3,4)
zeroes = np.zeros((2,2,2))
full = np.full((2,2,2), 7)
ones = np.ones((2,2,2))

print(data)
print(zeroes)

# Creating our own custom array
arr = np.array([[1,2,3,4], [1,2,3,4]])
print(arr)

print(type(arr))


# Reading our own arrays
shape = data.shape
size = data.size
types = data.dtype

# Updating 
list1 = np.random.rand(10)
list2 = np.random.rand(10)
print(list1)

data.sort()
print(data)
print('done sorted')
data = data.reshape((2,2,-1))
print(data)                 

print('Deleting')

# Deleting
# axis = 1 states that its a row
# 0 states the first row
data = np.delete(data, 0 , axis=1)
print(data)