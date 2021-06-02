import numpy as np



narray = np.array([1, 2, 3, 4])
print(np.flip(narray))


mat = np.matrix([[1, 2],
                 [3, 4]])
print(np.flip(mat))                     # flip the matrix along all axes
print(np.flip(mat, axis=0))             # flip the matrix along axis 0
print(np.flip(mat, axis=1))             # flip the matrix along axis 1
