import numpy as np

ar = np.array([1, 2, 3, 4, 5, 6, 7])

a = np.append(ar, 81)
print("1D Array Diagonal values : \n", a)
 
ar = np.array( [ [1, 2, 3],[ 4, 5, 6] ])
print("2D arr : \n", ar)

a = np.append(ar, [22, 23, 24])
print("2D Array diagonal values : \n", a)

