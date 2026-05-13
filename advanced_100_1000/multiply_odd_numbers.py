numbers = [9, 18, 15, 3, 35, 14, 8]
new_numbers = [num * 3 for num in numbers if num % 2 != 0]
# only multiply numbers by 3

print(', '.join(map(str, new_numbers)))