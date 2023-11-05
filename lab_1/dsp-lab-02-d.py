# encoding utf-8
# python 3.12

import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

np.random.seed(2023)

n = np.arange(-10, 11, 1)
x1 = np.random.uniform(-1, 1, 21)
x2 = np.random.uniform(-1, 1, 21)

plt.subplot(3, 1, 1)
plt.stem(n, x1)
plt.title('$ x1 $')
plt.xlabel('$ n $')
plt.ylabel('$ x1 $')

plt.subplot(3, 1, 2)
plt.stem(n, x2)
plt.title('$ x2 $')
plt.xlabel('$ n $')
plt.ylabel('$ x2 $')

x4 = np.roll(np.flip(x2), 3)
x4[0:3] = 0

plt.subplot(3, 1, 3)
plt.stem(n, x4)
plt.title('$ x4 $')
plt.xlabel('$ n $')
plt.ylabel('$ x4 $')

plt.show()
