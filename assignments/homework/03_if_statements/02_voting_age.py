PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user is old enough to vote
    if user_age < 16:
        print("You are too young to vote. (Min age is 16).")
    elif user_age < 25:
        print(f"You can vote in PETURKSBOUIPO (Min Age: {PETURKSBOUIPO_AGE}).")
    elif user_age < 48:
        print(f"You can vote in STANLAU (Min Age: {STANLAU_AGE}) & PETURKSBOUIPO (Min Age: {PETURKSBOUIPO_AGE}).")
    else:
        print(f"You can vote in MAYENGUA (Min Age: {MAYENGUA_AGE}), STANLAU (Min Age: {STANLAU_AGE}) & PETURKSBOUIPO (Min Age: {PETURKSBOUIPO_AGE}).")

if __name__ == "__main__":
    main()
