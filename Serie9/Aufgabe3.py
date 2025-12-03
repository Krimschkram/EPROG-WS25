import math
import matplotlib.pyplot as plt


x = [i * 0.1 for i in range(100)]
y = [math.sin(xi) for xi in x]

plt.plot(x, y)
plt.title('Linienplot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()