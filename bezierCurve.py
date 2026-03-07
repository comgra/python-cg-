import matplotlib.pyplot as plt
plt.ion()   
x0, y0 = 0, 0
x1, y1 = 1, 2
x2, y2 = 3, 0
xs = []
ys = []

plt.scatter([x0, x1, x2], [y0, y1, y2], color='red')

for t in [i/100 for i in range(101)]:
    x = (1-t)*(1-t)*x0 + 2*(1-t)*t*x1 + t*t*x2
    y = (1-t)*(1-t)*y0 + 2*(1-t)*t*y1 + t*t*y2
    xs.append(x)
    ys.append(y)
    plt.plot(xs, ys, 'b')
    plt.pause(0.01)   
plt.ioff()
plt.show()
