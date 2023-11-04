# encoding utf-8

import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

n = np.arange(-10, 11, 1)
delta_n = np.concatenate(
    (np.zeros([1, 10]), np.ones([1, 1]), np.zeros([1, 10])),
    axis=1
)

plt.stem(n, delta_n.transpose())
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Unit Sample Sequence')
plt.axis([-10, 10, 0, 1.2])
plt.show()
