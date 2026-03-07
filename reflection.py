import matplotlib.pyplot as plt
x = [1, 3, 2,1]
y = [1, 1, 3,1]
y_x = [-i for i in y]
plt.plot(x , y , 'r', label='Original')
plt.plot(x , y_x , 'b', label='X-axis')
plt.legend()
plt.axis('equal')
plt.title("Reflection Transformation across x-axis Example")
plt.show()
