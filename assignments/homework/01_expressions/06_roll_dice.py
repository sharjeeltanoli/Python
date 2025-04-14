import random

NUM_SIDES = 6

def main():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    total = die1 + die2
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
