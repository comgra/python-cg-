import matplotlib.pyplot as plt
import math
x = [1, 2, 3,1]
y = [1, 3, 1,1]
sx = 2   
sy = 1.5 
x_new = [i * sx for i in x]
y_new = [i * sy for i in y]
angle = 45
r = math.radians(angle)
x_rot = []
y_rot = []
for i in range(len(x_new)):
    x_rot.append(x_new[i]*math.cos(r) - y_new[i]*math.sin(r))
    y_rot.append(x_new[i]*math.sin(r) + y_new[i]*math.cos(r))
tx = 2  
ty = 1  
x_tran = [i + tx for i in x_rot]
y_tran = [i + ty for i in y_rot]
plt.plot(x, y, 'bo-', label='Original')
plt.plot(x_tran, y_tran, 'ro-', label='Composite Transformed')
plt.axis('equal')
plt.legend()
plt.title('Composite Transformation')
plt.show()
