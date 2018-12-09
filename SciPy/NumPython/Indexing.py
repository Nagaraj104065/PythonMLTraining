import numpy as np

a = np.arange(4)
print(a)

i = np.array([2, 2, 3])
print(a[i])

b = np.ones((3, 3, 3))
print(b)
print(b[0:2, 0:2])  # 2 rows 2 columns

c = np.array([[1, 2, 3], [4, 5, 6], [8, 9, 0]]);
print c[0:3, 2]

d = np.array([[[1, 2, 3], [4, 5, 6], [8, 9, 0]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
              [[21, 22, 23], [24, 25, 26], [28, 29, 30]], [[111, 112, 113], [114, 115, 116], [117, 118, 119]]])
print d[:1, 0:1]
print(d.ravel())
