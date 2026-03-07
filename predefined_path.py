import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

dot, = ax.plot(0, 5, 'ro')
i = 0
while True:
    if not plt.fignum_exists(fig.number):
        break
    
    x = 0 + 0.01 * i
    y = 5
    dot.set_data([x], [y])
    plt.draw()
    plt.pause(0.01)
    i += 1
    if x >= 10:     
        i = 0
plt.ioff()
print("Figure closed. Program ended.")
