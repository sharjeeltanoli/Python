import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for _ in range(N_NUMBERS):
        random_number: int = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number, end=" ")

if __name__ == "__main__":
    main()
