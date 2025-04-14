#speed of light
C = 299792458

def main():
    mass_in_kg = float(input("Enter mass in kg: "))
    energy = mass_in_kg * C**2

    print("e = m c²")
    print(f"m = {mass_in_kg} kg")
    print(f"c = {C} m/s")

    print(f"{energy} Joules of energy")

if __name__ == "__main__":
    main()
    

