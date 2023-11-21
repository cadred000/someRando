import numpy as np
import matplotlib as plt

def tent_map(mu, x):
    return mu * min(x, 1 - x)

def find_period(sequence, tolerance=1e-4):
    if any(x < 0 or x > 1 for x in sequence[-10:]):
        return -1
    
    if np.std(sequence[-5:]) < tolerance:
        return 0
    
    max_period = 128
    seq_length = len(sequence)
    for period in range(1, max_period + 1):
        is_periodic = True
        for i in range(period):
            for j in range(i + period, seq_length, period):
                if abs(sequence[i] - sequence[j]) > tolerance:
                    is_periodic = False
                    break
            if not is_periodic:
                break
        if is_periodic:
            return period
    return None 

mu_values = np.linspace(0.9, 1.2, 50)
mu_values = np.append(mu_values, [1.000, 2.000])
mu_values = np.unique(np.sort(mu_values))

print("The following is a discription of the behavior of the tent map for various values of mu.")
for mu in mu_values:
    x = 0.5
    sequence = [x]
    for _ in range(10000):
        x = tent_map(mu, x)
        sequence.append(x)
    period = find_period(sequence)
    if period == -1:
        print(f"Mu = {mu:.3f}: Diverges")
    elif period == 0:
        print(f"Mu = {mu:.3f}: Converges to zero")
    elif period is None:
        print(f"Mu = {mu:.3f}: Chaotic or aperiodic behavior")
    else:
        print(f"Mu = {mu:.3f}: Period-{period} behavior")
