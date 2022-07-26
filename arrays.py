from array import *
from multiprocessing.dummy import Array 

# value = array('i',[3,5,-7,4,9,8])
# value = array('u',['h','a','r','s','h','i','t'])
# value = array('I',[3,5,7,4,9,8])
# print(value)
# print(value.buffer_info())
# for i in range(0,5):
# for i in range(len(value)):
#     print(value[i])
# array = array('i',[])
# n = int(input("Enter the length of the array: "))

# for i in range(n):
#     x = int(input("Enter value for array: "))
#     array.append(x)

# print(array)

# value = int(input("Enter the number for search: "))
# k=0
# for e in array:
#     if e == value:
#         print(k)
#         break
#     k+=1


arr = array('i',[])
n = int(input("Enter the length of array:  "))

for i in range(n):
    x = int(input("Enter the value of array: "))
    arr.append(x)
print(arr)

x = int(input("Value to search: "))
k=0
for j in arr:
    if j == x:
        print(k)
        break
    k+=1