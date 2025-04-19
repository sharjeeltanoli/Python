def main():
    my_list = []
    element: str = input("Enter a value to add to the list: ")
    while element:
        my_list.append(element)
        element = input("Enter a value or press Enter to finish: ")
    print("The list is:")
    print(my_list)

if __name__ == "__main__":
    main()
    
# The code above is a simple program that collects user input and stores it in a list.