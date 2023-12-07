import numpy as np
import datetime

def tent_map(mu, x):
    return mu * min(x, 1 - x)
    

def generate_rando():
    ms = datetime.datetime.now().microsecond
    x = max((0.5 * ms) % 1, 0.000001)
    iterations = 200 * max(datetime.datetime.now().second, 1)
    for _ in range(iterations):
        x = tent_map(1.95, x) 

    return x

print("\n******** Welcome to my Pseudo-Random Number Generator! ********\n")
print("This program generates a unique random number on [0, 1).\n")

while True:
    rando = generate_rando()
    print(f"Your Unique Random Number: {rando}")

    play_again = input("\nWould you like another number? (y/n): ").strip().lower()
    if play_again != 'y':
        break

print("\nThanks for playing! Go Devils!!!\n\n")
