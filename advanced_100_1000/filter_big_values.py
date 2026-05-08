nums = [10, 15, 20, 25]
big_values = list(filter(lambda x: x > 20, nums))
result = ', '.join(map(str, big_values))
print(result)