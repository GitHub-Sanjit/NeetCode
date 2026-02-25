def add_two_numbers() -> int:
    numbers_line = input()
    numbers = numbers_line.split(",")
    result = 0
    for (num) in numbers:
        n = int(num)
        result = result + n
    return result



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
