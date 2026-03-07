# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all odd numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.

def remove_odd(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


original_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_odd(original_list)

print("Original list:", original_list)
print("List without odd numbers:", new_list)