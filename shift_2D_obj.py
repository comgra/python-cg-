import matplotlib.pyplot as plt
x = [1, 2, 3,1]
y = [1, 3, 1,1]
tx = 2  
ty = 1  
x_new = [i + tx for i in x]
y_new = [i + ty for i in y]
plt.plot(x , y , 'r-o',label='Original')
plt.plot(x_new , y_new , 'b-o',label='Translated')
plt.legend()
plt.axis('equal')  
plt.show()
