# encoding utf-8
# python 3.12

import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

n = np.arange(-20, 21)
a1 = 1.5
a2 = 0.5


def x(n, a):
    return float(a) ** n * (n >= 0)


plt.subplot(2, 2, 1)
plt.stem(n, x(n, a1))
plt.title('$ \\vert a \\vert > 1, a = {a1} $')
plt.xlabel('$ n $')
plt.ylabel('$ x(n) $')

plt.subplot(2, 2, 2)
plt.stem(n, x(n, -a1))
plt.title('$ \\vert a \\vert < 1, a = -{a1} $')
plt.xlabel('$ n $')
plt.ylabel('$ x(n) $')

plt.subplot(2, 2, 3)
plt.stem(n, x(n, a2))
plt.title('$ \\vert a \\vert > 1, a = {a2} $')
plt.xlabel('$ n $')
plt.ylabel('$ x(n) $')

plt.subplot(2, 2, 4)
plt.stem(n, x(n, -a2))
plt.title('$ \\vert a \\vert < 1, a = -{a2} $')
plt.xlabel('$ n $')
plt.ylabel('$ x(n) $')

plt.show()
