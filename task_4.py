import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
plt.plot(x, np.cos(1*x), marker="o")
plt.plot(x, np.cos(-0.5*x), marker="o")
plt.show()
