import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [15, 8, 12, 4, 6]
labels = ['A', 'B', 'C', 'D', 'E'] 
colors = ['red', 'yellow', 'blue', 'black', 'orange'] 
markers = ['o', 's', '^', 'v', 'x']  
for i in range(len(x)):
    plt.scatter(x[i], y[i], c=colors[i], marker=markers[i], label=labels[i])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Labeled Data Points')

plt.legend()

plt.show()