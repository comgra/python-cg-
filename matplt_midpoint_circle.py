import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    X, Y = [], []

    while x <= y:
        X += [xc + x, xc - x, xc + x, xc - x, xc + y, xc - y, xc + y, xc - y]
        Y += [yc + y, yc + y, yc - y, yc - y, yc + x, yc + x, yc - x, yc - x]

        if p < 0:
            p += 2 * x + 3
            x += 1
        else:
            p += 2 * (x - y) + 5
            x += 1
            y -= 1

    return X, Y

X, Y = midpoint_circle(0, 0, 5)
plt.scatter(X, Y)
plt.gca().set_aspect('equal')
plt.show()
