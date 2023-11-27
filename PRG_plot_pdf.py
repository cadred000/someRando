import numpy as np
import matplotlib.pyplot as plt

def tent_map(mu, x):
    if x < 0.5:
        return mu * x
    else:
        return mu * (1 - x)

def generate_data(mu, n_iterations=1000, n_points=1000):
    data = []
    x = 0.5
    for _ in range(n_iterations):
        x = tent_map(mu, x)
        data.append(x)
    return data

mus = [1.1, 1.25, 1.39] 
n_bins = 12 

plt.figure(figsize=(12, 6))

for mu in mus:
    data = generate_data(mu)
    plt.hist(data, bins=n_bins, density=True, alpha=0.5, label=f'mu={mu}')

plt.title('Tent Map Density')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()