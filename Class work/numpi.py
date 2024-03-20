
import numpy as np
'''
#creating an array using np.array() method
#single-dimension array
arr = np.array([10,20,30,40,50])
print(arr)

# multi-dimension array
arr2 = np.array([[1, 2], [3, 4], [5,6],[8,7],[9,10]]) 
print(arr2)

#using minimum dimension parameter
arr3 = np.array([1, 2, 3, 4, 5], ndmin = 2) 
print(arr3)

# using dtype parameter  
arr4 = np.array([1, 2, 3], dtype = complex) 
print(arr4)
'''
#Array iteration
arr5 = np.arange(0,60,5) #creates an ordered array
arr5 = arr5.reshape (3,4) #3 rows 4 columns 
print ("original array is: \n", arr5, "\n")
print ("Modified array is: ")
for x in np.nditer(arr5):
    print(x)

