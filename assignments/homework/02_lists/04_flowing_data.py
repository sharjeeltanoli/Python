def add_list(my_list, new_item):
    
    for i in range(3):
        my_list.append(new_item)

def main():

    message = input("Enter a value to add to the list: ")
    my_list = []

    print("Before adding:", my_list)
    add_list(my_list, message)

    print("After adding:", my_list)

if __name__ == "__main__":
    main()