import matplotlib.pyplot as pl
import numpy as np


# pl.plot([1, 2, 3, 4])
a = np.arange(0, 10, 0.01)
s = a*np.sin(a)
pl.plot(a, s)
pl.ylabel('some numbers')
pl.show()
