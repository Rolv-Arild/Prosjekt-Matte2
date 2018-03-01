import matplotlib.pyplot as pl
import numpy as np


# pl.plot([1, 2, 3, 4])
a = np.arange(-10, 10, 0.01)
x = a ** 2
pl.plot(a, x)
pl.ylabel('some numbers')
pl.show()
