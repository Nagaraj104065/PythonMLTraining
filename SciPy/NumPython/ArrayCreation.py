import numpy as np

a = np.array([1, 2, 3], dtype=np.float32)
print a

b = np.zeros((1, 3, 3), dtype=np.float32)
print(b)

c = np.arange(0, 10, 2)
print c

c = np.arange(0, 15).reshape(3, 5)
print c

from numpy import pi

np.linspace(0, 2, 9)  # 9 numbers from 0 to 2
x = np.linspace(0, 2 * pi, 100)  # useful to evaluate function at lots of points
f = np.sin(x)

print x
print f
