import numpy as np
import matplotlib.pyplot as plt

def tent_map(mu, x):
    if x < 0.5:
        return mu * x
    else:
        return mu * (1 - x)

x_values = np.linspace(0, 1, 400)  
mu = 1  

y_values = [tent_map(mu, x) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'Tent Map with mu={mu}')
plt.xlabel('x')
plt.rc('text', usetex=False)
plt.title('Tent Map\n $T(x) = \mu x,\ x\ <\ 0.5;\ T(x) = \mu (1 - x),\ x\ \geq\ 0.5$')
plt.ylabel('T(x)')
plt.grid(True)
plt.legend()
plt.show()