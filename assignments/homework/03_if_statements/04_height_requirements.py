MIN_HEIGHT: int = 50

def main():
    
    try:
        height: int = int(input("Enter tall are you!"))
        if height >= MIN_HEIGHT:
            print("You are tall enough to ride!")
        else:
            print("You are not tall enough to ride!")
    except ValueError:
        print("Please enter a valid number for height.")

if __name__ == "__main__":
    main()


    
