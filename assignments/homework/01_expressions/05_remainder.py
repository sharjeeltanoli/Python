def main():

    dividend: int = int(input("Enter the dividend: "))
    divisor: int = int(input("Enter the divisor: "))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print(f"The Result of Division is: {quotient} and the Remainder is: {remainder}")

if __name__ == "__main__":
    main()
