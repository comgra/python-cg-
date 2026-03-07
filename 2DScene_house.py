import matplotlib.pyplot as plt

plt.fill([1, 1, 3, 3], [0, 2, 2, 0], color='orange')    
plt.fill([1, 2, 3], [2, 3, 2], color='brown')           
plt.fill([4, 4.2, 4.2, 4], [0, 0, 1, 1], color='saddlebrown')  
circle = plt.Circle((4.1, 1.5), 0.5, color='green')            
plt.gca().add_patch(circle)

sun = plt.Circle((0.5, 3.5), 0.4, color='yellow')
plt.gca().add_patch(sun)

plt.xlim(0, 5)
plt.ylim(0, 4)
plt.axis('off')
plt.show()
