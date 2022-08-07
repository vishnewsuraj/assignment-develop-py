import copy
# Shallow copy

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newData = copy.copy(data)

newData[0][2] = 'c'
print('New Shallow copy data : {}'.format(newData))
print('Previous data : {}'.format(data))

# Deep copy

newDeepCopy = copy.deepcopy(data)
newDeepCopy[0][2] = 'c'
print('New deep copy data : {}'.format(newDeepCopy))
print('Previous data : {}'.format(data))