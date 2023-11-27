import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

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

mus = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
skewness_values = []

for mu in mus:
    data = generate_data(mu)
    skewness = skew(data)
    skewness_values.append(skewness)

plt.figure(figsize=(8, 6))
plt.plot(mus, skewness_values, marker='o', linestyle='-')
plt.title('Skewness of Tent Map Data for Different Mu Values')
plt.xlabel('Mu')
plt.ylabel('Skewness')
plt.grid(True)
plt.show()