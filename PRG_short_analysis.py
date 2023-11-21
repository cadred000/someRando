import numpy as np

def tent_map(mu, x):
    return mu * min(x, 1 - x)

def find_period(sequence, tolerance=1e-10):
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

    normalized_seq = sequence - mean_val
    autocorr = np.correlate(normalized_seq, normalized_seq, mode='full')
    autocorr_norm = autocorr[len(sequence)-1:-1] / autocorr[len(sequence)-1]
    
    return mean_val, std_dev, variance, autocorr_norm

chaotic_mu_values = []
chaotic_sequences = []

mu_values = np.linspace(1, 2, 1000)
for mu in mu_values:
    x = 0.75
    sequence = []
    for _ in range(50000):
        x = tent_map(mu, x)
        sequence.append(x)
    
    period = find_period(sequence)
    if period is None: 
        chaotic_mu_values.append(mu)
        chaotic_sequences.append(sequence)

total_mean, total_std_dev, total_variance, total_autocorr = 0, 0, 0, np.zeros(9999)
num_chaotic_sequences = len(chaotic_sequences)

for sequence in chaotic_sequences:
    mean_val, std_dev, variance, autocorr_norm = analyze_chaos(sequence)
    total_mean += mean_val
    total_std_dev += std_dev
    total_variance += variance 

avg_mean = total_mean / num_chaotic_sequences
avg_std_dev = total_std_dev / num_chaotic_sequences
avg_variance = total_variance / num_chaotic_sequences
avg_autocorr = np.mean(total_autocorr[1:] / num_chaotic_sequences)  

print("The following are the statistics for the chaotic sequences of the tent map.\nThey are taken from 1000 values of 1 < mu < 2,\niterated 50000 times each, with a value of x = 0.75")
print(f"Average Mean: {avg_mean:.3f}")
print(f"Average Standard Deviation: {avg_std_dev:.3f}")
print(f"Average Variance: {avg_variance:.3f}")
print(f"Average Autocorrelation: {avg_autocorr:.3f}")


