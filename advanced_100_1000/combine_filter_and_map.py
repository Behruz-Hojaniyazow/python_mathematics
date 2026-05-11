nums = [9, 78, 56, 4, 3, 74]
new_nums = list(
  map(lambda x: x * 10,
  filter(lambda x: x % 2 == 0, nums))
)
print(', '.join(map(str, new_nums)))