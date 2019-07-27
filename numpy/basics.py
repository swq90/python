import numpy as np
from numpy import *
b = np.floor(10*np.random.random((1,5)))

a = np.floor(10*np.random.random(1,5))
print(b,a)
print(column_stack((a,b)))

c.flags.owndata