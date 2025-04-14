# Pythagorean theorem

import math

def main():
    # getting the lengths of two sides of triangle
    ab: float = float(input(" \033[1;3m Enter the length of side AB: "))
    ac: float = float(input("Enter the length of side AC: "))

    # calculating the length of the two sides
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"The length of side BC is \033[0m {bc:.2f} ")

if __name__ == "__main__":
    main()
    