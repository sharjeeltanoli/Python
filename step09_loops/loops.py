# for loops using list
fruits = ["apple", "banana", "orange", "cherry"]
for fruit in fruits:
    print(fruit)

# for loops getting index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# for loops using range
for i in range(1, 6):
    print(i)

# for loops using range(start, stop, step)
for i in range(1, 12, 3): # start at 1, stop before 12, step by 3
    print(i)

# while loops
count = 10
while count >= 1:
    print(count)
    count -= 1 # decrement count by 1

# guess the number
correct_number = 6
guess = 0
while guess != correct_number:
    guess = int(input("Guess the number between 1 to 9: "))
    print("Try again" if guess != correct_number else "You win!")
    