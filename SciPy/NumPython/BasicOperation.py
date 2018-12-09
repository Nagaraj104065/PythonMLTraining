import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print b
c = a - b
print c
print b ** 2
print 10 * np.sin(a)
print a < 35

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print A * B  # elementwise product
print A.dot(B)  # matrix product
print np.dot(A, B)  # another matrix product

a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print a


a = np.random.random((2,3))
print a

print a.sum()

print a.min()
print a.max()

