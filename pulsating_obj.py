import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, color='blue')
ax.add_patch(circle)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
i = 0
while True:
    if not plt.fignum_exists(fig.number):
        break
    r = 1 + 0.5 * np.sin(i * 0.2)
    circle.set_radius(r)
    plt.draw()
    plt.pause(0.05)
    i += 1
plt.ioff()
print("Figure closed. Program ended.")
