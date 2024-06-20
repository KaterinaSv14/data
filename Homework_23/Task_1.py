
import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = [2 * i + 1 for i in x]

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()

