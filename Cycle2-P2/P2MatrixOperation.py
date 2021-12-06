import numpy as np
m=np.arange(1,10).reshape(3,3)
print(m)

print("Cube using multiply():")
print(np.multiply(m,3))

print("Cube using * ")
print(m*m*m)

print("Cube using power(): ")
print(np.power(m,3))

print("Cube using ** : ")
print(m**3)