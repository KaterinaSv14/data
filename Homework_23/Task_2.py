
import random
import matplotlib.pyplot as plt

data = [random.normalvariate(0, 1) for _ in range(1000)]

plt.hist(data, bins=30, edgecolor='blue', alpha=0.7)

plt.show()
