import numpy as np

def tent_map(mu, x):
    return mu * min(x, 1 - x)

def generate_rando(start, end, mu=1.5, iterations=100000):
    x = np.random.uniform(0.5, 0.9)
    for _ in range(iterations):
        x = tent_map(mu, x)
    
    normalized = start + int(x * (end - start+1))
    return normalized

while True:
    start_val = int(input("\nEnter an integer value to start the range: "))
    end_val = int(input("Enter an integer value to end the range: "))
    
    if np.abs(end_val - start_val) >= 2:
        rando = generate_rando(start_val, end_val)
        print(f"Your Unique Random Number: {rando}")
    else:
        print("\n***** Invalid Entry. Range interval must be greater than 1 *****")
    
    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        break

print("\nThanks for playing! Go Devils!!!\n\n")