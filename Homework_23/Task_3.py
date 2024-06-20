import matplotlib.pyplot as plt
import math

x = [i / 100 * 2 * math.pi for i in range(100)]
y_sin = [math.sin(i) for i in x]
y_cos = [math.cos(i) for i in x]

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) and cos(x)')

plt.show()
