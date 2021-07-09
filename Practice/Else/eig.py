import numpy as np

M1 = np.matrix([[1, 0, -1],[-1, 0, 1]])
M2 = M1.T
print(M2.dot(M1))
M3 = np.matrix([[4, 4, 0], [4, 8, 4], [0, 4, 4]])
print(np.linalg.matrix_rank(M3))
print(np.linalg.matrix_rank(M2.dot(M1)))
eig_val, eig_vec = np.linalg.eig(M2.dot(M1))
print(eig_val)
print(eig_vec)

eig_val, eig_vec = np.linalg.eig(M3)
print(eig_val)
