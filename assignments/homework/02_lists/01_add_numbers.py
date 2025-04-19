def add_many(numbers) -> int:

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    
    return total_so_far

def main():
    numbers = [1, 2, 3, 4, 5]
    sum: int = add_many(numbers)
    print(sum)

if __name__ == "__main__":
    main()
