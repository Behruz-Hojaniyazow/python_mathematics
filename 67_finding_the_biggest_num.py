def find_max(numbers):
  """a function that finds the biggest number in the list"""
  max_val = numbers[0]
  for num in numbers:
    if max_val > num:
      max_val = num
  return max_val
my_list = [12, 34, 3, 7, -3, 45, 36]
result = find_max(my_list)
print(f"The biggest number in the list is {result}")