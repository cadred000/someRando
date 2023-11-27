import numpy as np
import matplotlib.pyplot as plt

def tent_map(mu, x):
    return mu * min(x, 1 - x)

def generate_bifurcation_data(mu_values, n_iterations=1000, n_last=100):
    x_values = []
    mu_list = []

    for mu in mu_values:
        x = 0.5  
        for i in range(n_iterations):
            x = tent_map(mu, x)
            if i >= n_iterations - n_last:
                x_values.append(x)
                mu_list.append(mu)

    return mu_list, x_values

mu_values = np.linspace(1, 2, 10000)  
n_iterations = 1000  
n_last = 100  

mu_list, x_values = generate_bifurcation_data(mu_values, n_iterations, n_last)

plt.figure(figsize=(10, 6))
plt.plot(mu_list, x_values, ',k', alpha=0.5)
plt.title('Bifurcation Diagram for the Tent Map')
plt.xlabel('$\mu$')
plt.ylabel('x')
plt.show()