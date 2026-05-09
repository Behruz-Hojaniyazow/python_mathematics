numbers = list(range(1,11))
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
result = ', '.join(map(str, even_nums))
print(result)