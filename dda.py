x1, y1 = 2, 2
x2, y2 = 8, 5
dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))  
Xinc = dx / steps
Yinc = dy / steps

x = x1
y = y1
print("Line points:")
for i in range(steps + 1):
    print(round(x), round(y))  
    x += Xinc
    y += Yinc

import matplotlib.pyplot as plt
x = [2, 3, 4, 5, 6, 7, 8]
y = [2, 2, 3, 3, 4, 4, 5]
plt.plot(x, y)
plt.show()
