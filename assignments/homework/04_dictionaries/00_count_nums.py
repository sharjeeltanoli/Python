def get_numbers():
    my_list = []

    while True:
        add_numers = input("Type a number or Press Enter to finish: ")
        if add_numers == "":
            print(my_list)
            break
        try:
            my_list.append(int(add_numers))
        except ValueError:
            print("Please enter a valid number")
        continue
    return my_list

def count_nums(nums_list):
    num_dict = {}
    for num in nums_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_nums(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times")

def main():
    nums_list = get_numbers()
    num_dict = count_nums(nums_list)
    print_nums(num_dict)

if __name__ == "__main__":
    main()
    