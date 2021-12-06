import numpy as np
m=np.arange(1,10).reshape(3,3)
print("Matrix:\n ",m)

print("Cube using multiply():\n",np.multiply(m,3))

print("Cube using * :\n ",m*m*m)

print("Cube using power():\n",np.power(m,3))

print("Cube using ** :\n",m**3)

print("Identity matrix of the given square matrix:")
print(np.identity(3,dtype= int))

print(" Display each element of the matrix to different powers.")
print(np.power(m,m))

print("Create a matrix Y with same dimension as X and perform the operation X2+2Y:",)
