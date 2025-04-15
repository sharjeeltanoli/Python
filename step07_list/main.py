#List
#          0          1         2        3       4       -> left to right index |  positive index
#         -5        -4        -3        -2      -1       <- right to left index |  negative index 
items = ["apple", "banana", "cherry", "mango", "grapes"]

#getting all the items in the list
print(f"all Items: {items}" )

#get the length of the list
print("Length of item:", len( items ))

#getting the first item in the list
print( "first item:", items[0] ) # apple

#getting the last item in the list
print( "last item:", items[-1] ) # grapes

#list Slicing

print("Slicing items:", items[1:3] ) # ['banana', 'cherry']

#Checking if an item is in the list
print( "apple" in items ) # True
print( "orange" in items ) # False

#Adding items to the list
items.append("orange") # adding at the end of the list
print("After adding orange:", items )

#Adding items at a specific index
items.insert(2, "kiwi") # adding at index 2
print("After adding at index 2:", items )

#Removing items from the list
items.remove("banana") # removing by value
print("After removing banana:", items )

items.pop() # removing the last item
print("After removing last item:", items )

items.pop(1) # removing item at index 1
print("After removing item at index 1:", items )


