# 3 - simple plot
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1
# y = x**2
plt.plot(x, y)
plt.show()