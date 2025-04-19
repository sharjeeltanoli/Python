def get_element(my_list):

    print(my_list[-1])  # Access the last element


def get_list():
    my_list = []
    element: str = input("Enter a value to add to the list: ")
    while element != "":
        my_list.append(element)
        element = input("Enter a value or press Enter to finish: ")
    return my_list

def main():
    my_list = get_list()
    print("The last element of the list is:")
    get_element(my_list)

if __name__ == "__main__":
    main()
