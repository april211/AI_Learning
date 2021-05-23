import numpy as np
import matplotlib.pyplot as plt


n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2* X)

plt.axes([0.025,0.025,0.95,0.95])

# The alpha channel can be used to soften colors for more visually appealing plots.
plt.plot (X, Y+1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y+1, color='blue', alpha=.25)

plt.plot (X, Y-1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)

plt.xlim(-np.pi, np.pi), plt.xticks([])         # Passing an empty list removes all xticks
plt.ylim(-2.5, 2.5), plt.yticks([])

plt.show()


# https://matplotlib.org/3.3.4/gallery/recipes/fill_between_alpha.html
