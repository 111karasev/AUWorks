import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

iterations=20

def my_asin(x):
    x_pow=x
    multiplier=1
    partial_sum=x
    for n in range(1, iterations):
        x_pow *= x**2
        b_multiplier=0
        multiplier *= (2*n)/(n**2)
        b_multiplier =multiplier/(4**n)/(2*n+1)
        partial_sum += x_pow * b_multiplier
    return partial_sum
print(help(math.asin), math.asin(0.4))
print(help(my_asin), my_asin(0.4))
angles = np.r_[-1:1:0.001]
plt.plot(angles, np.arcsin(angles))
plt.plot(angles, np.vectorize(my_asin)(angles))
plt.show()
