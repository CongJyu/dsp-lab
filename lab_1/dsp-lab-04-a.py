# encoding utf-8
# python 3.10

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def x_a(t):
    return t * np.exp(-t) * (t >= 0)


def X_a(w):
    return 1 / ((1 + 1j * w) ** 2)


system = signal.lti([], X_a)
t, y = signal.impulse(signal, N=1000)  # the sentence is strange

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
t1 = np.linspace(0, 10, 1000)
plt.plot(t1, x_a(t1), label='$ x_a(t) $')
plt.xlabel('$ t $')
plt.ylabel('$ x_a(t) $')
plt.legend()

plt.subplot(t, y, label='Impulse Response')
plt.xlabel('$ t $')
plt.ylabel('$ y(t) $')
plt.legend()

plt.show()
