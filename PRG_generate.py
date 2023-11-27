import numpy as np
from decimal import Decimal, ROUND_HALF_UP
import datetime

count = 0

def tent_map(mu, x):
    return mu * min(x, Decimal('1') - x)

def generate_rando(start, end, count, mu=Decimal('1.95')):
    x = Decimal('0.5')
    iterations = 99997 * (datetime.datetime.now().minute) + count
    for _ in range(iterations):
        x = tent_map(mu, x)

    normalized = start + x * (end - start)
    rounded = normalized.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return rounded

print("\n******** Welcome to my Pseudo-Random Number Generator! ********\n")
print("This program generates a unique random number within a given range.")
while True:
    start_val = int(input("\nEnter an integer value to start the range: "))
    end_val = int(input("Enter an integer value to end the range: "))

    if np.abs(end_val - start_val) >= 2:
        rando = generate_rando(start_val, end_val, count)
        count += 1
        print(f"Your Unique Random Number: {rando}")
    else:
        print("\n***** Invalid Entry. Range interval must be greater than 1 *****")

    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        break

print("\nThanks for playing! Go Devils!!!\n\n")
