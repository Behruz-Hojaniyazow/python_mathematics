numbers = list(range(11))
string_nums = ['EVEN' if num % 2 == 0 else 'ODD' for num in numbers]
print(', '.join(string_nums))