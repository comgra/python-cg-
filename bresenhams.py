def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    p = 2 * dy - dx
    points = [(x, y)]
    for i in range(dx):
        if p < 0:
            x += 1
            p = p + 2 * dy
        else:
            x += 1
            y += 1
            p = p + 2 * (dy - dx)
        points.append((x, y))
    return points
line_points = bresenham_line(2, 2, 8, 5)
print("Line points:")
for p in line_points:
    print(p)

import matplotlib.pyplot as plt
x = [2,3,4,5,6,7,8]
y = [2,3,3,4,4,5,5]
plt.plot(x, y)
plt.show()
