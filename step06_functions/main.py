# simple function
def greet():
    # block of code
    print("Hello World!")
greet() # calling function 


#function with parameter
def welcome(name):
    print(f"Hello {name}!")
welcome("Khan")
welcome("Ali")


#function with default parameter
def welcome(name="guest"):
    print(f"Hello {name}!")
welcome()
welcome("Ali")


# function with return value
def add(a, b):
    return a + b
print(add(5, 10))


#Function with Multiple Arguments
def addition(*numbers):
    return sum(numbers)
print(addition(4, 5, 3, 10, 2))
