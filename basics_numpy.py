import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])


print()
arr[0:3]=10
print(arr)

print()
var1=np.reshape(arr,(3,5))
print(var1)

print()
var2=arr.flatten()
print(var2)


#To create a 1d array between a range
var3=np.arange(1,11).reshape((5,2))
print(var3)

#To create an array with given shape and random integers from a given range
var4=np.random.randint(1,101,(10,6))
print(var4)
print()

#condition:both divisible by 3 and 7 ,also greater than 50
mask=(var4%3==0)&(var4>50)&(var4%7==0)
var4[mask]
print(var4[mask])
print()
print(var4)

