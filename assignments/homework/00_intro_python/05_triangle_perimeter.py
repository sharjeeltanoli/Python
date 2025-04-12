def main():

# prompt the user
    side1 = float(input("\033[1;3m Enter the length of the first side of the triangle: \033[0m"))
    side2 = float(input("\033[1;3m Enter the length of the second side of the triangle: \033[0m"))
    side3 = float(input("\033[1;3m Enter the length of the third side of the triangle: \033[0m")) 

    # respond to the user
    print("The perimeter of the triangle is " + str (side1 + side2 + side3))

# call the main function
if __name__ == "__main__":
    main()