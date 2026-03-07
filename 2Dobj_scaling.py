import matplotlib.pyplot as plt
x = [1, 2, 3,1]
y = [1, 3, 1,1]
sx = 2   # scale in x-direction
sy = 1.5 # scale in y-direction
x_new = [i * sx for i in x]
y_new = [i * sy for i in y]
plt.plot(x , y , 'r-o', label='Original')
plt.plot(x_new , y_new , 'b-o', label='Scaled')
plt.legend()
plt.axis('equal')
plt.title("Scaling Transformation Example")
plt.show()
