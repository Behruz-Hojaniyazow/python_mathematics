def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print('Please enter only numbers, Try again')
def multiply(*args):
  """a function that multiplies all numberss"""
  if not args:
    return 1
  num = 1
  for number in args:
    num *= number
  return num
while True:
  numbers = []
  choice = get_number("Enter a number (or 'done' to finish): ")
  if choice.lower() == "done":
    break
  try:
    numbers.append(choice)
  except ValueError:
    print("Invalid input, Try Again")
  if numbers:
    result = multiply(*numbers)
  number_str = " × ".join(map(str, numbers))
  print(f"{number_str} = {result}")
  if input("Do you wanna continue (yes/no)?").lower() == "no":
    break