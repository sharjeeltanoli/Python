MAX_LENGTH = 3

def shorten(my_list):
    # List to store deleted elements
    deleted_list = []  

    while len(my_list) > MAX_LENGTH:

        # Remove the last element from the list
        last_elem = my_list.pop()   

        # Add the removed element to the deleted list
        deleted_list.append(last_elem) 
    # Print the deleted elements             
    print(f"Removed {deleted_list} from the list")  

def add_list():
    my_list = []
    element: str = input("Enter a value to add to the list: ")
    while element != "":
        my_list.append(element)
        element = input("Enter a value or press Enter to finish: ")
    return my_list
    
def main():
    my_list = add_list()
    shorten(my_list)
    print("The list is:", my_list)
 

if __name__ == "__main__":
    main()