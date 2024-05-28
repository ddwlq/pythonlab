import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y = -x**np.cos(5*x)

plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x)=-x^cos(5*x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графік функції')
plt.legend()
plt.grid(True)
plt.show()
