#fahrenheit to celsius converter

def main():
    try:
        #p rompt the user
        fahrenheit = float(input("\033[1;3m Enter the temperature in Fahrenheit: \033[0m"))
        celsius = (fahrenheit - 32) * 5.0 / 9.0

        # respond to the user
        print(f"Temperature: {fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# call the main function
if __name__ == "__main__":
    main()


