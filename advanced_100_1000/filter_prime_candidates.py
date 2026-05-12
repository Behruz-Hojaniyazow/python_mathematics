nums = [12, 34, 57, 79, 3, 6, 65]
new_nums = list(
  filter(lambda num: num > 10 and num % 2 != 0, nums)
)
print(', '.join(map(str, new_nums)))