def remove_odd(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


original = [1, 2, 3, 4, 5, 6, 7, 8]

filtered = remove_odd(original)

print("Original list:", original)
print("Even numbers:", filtered)