def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers")
def fibonacci(n):
  """a function that finds the fibonacci"""
  if n <= 0:
    return []
  if n == 1:
    return [0]
  sequence = [0, 1]
  while len(sequence) < n:
    new_number = sequence[-1] + sequence[-2]
    sequence.append(new_number)
  return sequence
number = get_number("How many terms are needed?: ")
result = fibonacci(number)
print("=" * 30)
print(f"{number} terms are equal to {result}")
print("=" * 30)