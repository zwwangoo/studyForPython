import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

a2[1, 1] = 10
print(a2[:, 0])

print(a1)
print(a1.shape)
print(a2.shape)
print(a2.dtype)
print(a2)
