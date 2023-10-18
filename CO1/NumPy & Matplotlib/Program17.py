import numpy as np
import matplotlib.pyplot as plt
mean = 0
sd = 1
sample = 1000
data = np.random.normal(mean, sd, sample)
plt.hist(data, bins=30, density=True, alpha=0.5, color='red', edgecolor='blue')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / sd)**2)
plt.plot(x, pdf, 'k-', linewidth=2)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.show()