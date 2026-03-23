def sum_list(numbers: list):
    total = 0

    for num in numbers:
        total += num

    return total

my_list = [5, 10, 15, 20]

result = sum_list(my_list)

print("Sum is:", result)