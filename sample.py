import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

y1 = (np.random.random(100) - 0.5).cumsum()
y2 = y1.reshape(-1, 10).mean(axis=1)
print(len(y1))
print(len(y2))

x1 = np.linspace(0, 1, 100)
x2 = np.linspace(0, 1, 10)
print(len(x1))
print(len(x2))

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.show()