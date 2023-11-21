import numpy as np

def tent_map(mu, x):
    return mu * min(x, 1 - x)

def find_period(sequence, tolerance=1e-4):
    if any(x < 0 or x > 1 for x in sequence[-10:]):
        return -1
    
    if np.std(sequence[-5:]) < tolerance:
        return 0
    
    max_period = 32  
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

def analyze_chaos(sequence):
    mean_val = np.mean(sequence)
    std_dev = np.std(sequence)
    variance = np.var(sequence)

    return mean_val, std_dev, variance

chaotic_mu_values = []
chaotic_sequences = []
iterations = 50000

mu_values = np.linspace(1, 2, 500)
for mu in mu_values:
    x = 0.5
    sequence = []
    for _ in range(iterations):
        x = tent_map(mu, x)
        sequence.append(x)
    
    period = find_period(sequence)
    if period is None: 
        chaotic_mu_values.append(mu)
        chaotic_sequences.append(sequence)

print(f"The following is a sample of the statistics for chaotic sequences of the tent map.\nSample underwent {iterations} iterations with a value of x = 0.5")
sampled_indices = np.linspace(0, len(chaotic_mu_values) - 1, 20, dtype=int)
for index in sampled_indices:
    mu = chaotic_mu_values[index]
    sequence = chaotic_sequences[index]
    mean_val, std_dev, variance = analyze_chaos(sequence)
    print(f"Mu = {mu:.3f}: Mean = {mean_val:.3f}, Std Dev = {std_dev:.3f}, Variance = {variance:.3f}")


