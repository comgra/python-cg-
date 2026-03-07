import matplotlib.pyplot as plt
x = [1, 3, 2, 1]
y = [1, 1, 3, 1]
shx = 0.75   
shy = 0.0   
x_new = [x[i] + shx * y[i] for i in range(len(x))]   
y_new =[y[i] + shy * x[i] for i in range(len(y))]       
plt.plot(x, y, 'b-o', label='Original Triangle')
plt.plot(x_new, y_new, 'r-o', label='Sheared Triangle')
plt.axis('equal')
plt.legend()
plt.title('Shearing Transformation (Triangle)')
plt.show()
