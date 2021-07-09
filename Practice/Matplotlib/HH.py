from matplotlib import pyplot as plt
import numpy as np

plt.figure()
a = [1,2,5,6,9,11,15,17,18]
plt.hlines(1,1,20)  # Draw a horizontal line
plt.eventplot(a, orientation='horizontal', colors='r', linelengths=5)

plt.axis('off')
plt.show()
