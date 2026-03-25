def get_number(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers, Try again")
def find_minimum(a, b):
  if a < b:
    return a
  else:
    return b
num_a = get_number("Enter the (a): ")
num_b = get_number("Enter thr (b): ")
result = find_minimum(num_a, num_b)
print(f"The minimum number is:  {result}")