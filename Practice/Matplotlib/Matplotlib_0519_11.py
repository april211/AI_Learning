import matplotlib.pyplot as plt


# generate an axis object
ax = plt.axes([0.025,0.025,0.95,0.95])

# set the limitations of xaxis & yaxis of this ax
ax.set_xlim(0,4)
ax.set_ylim(0,3)

# set the major & minor locator of this axis
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

# distinguish the major & minor locator's lines on the xaxis by setting two different linewidths
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

# clear axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# savefig('../figures/grid_ex.png',dpi=48)
plt.show()
