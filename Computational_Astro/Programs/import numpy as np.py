import numpy as np
import matplotlib.pyplot as plt
fig6, ax = plt.subplots()

ax.add_patch(plt.Circle((0, 0), 1))
ax.set_aspect("equal")
ax.set_box_aspect(1)
ax.autoscale()
plt.xticks(range(0, 1, 0.2))
plt.show()