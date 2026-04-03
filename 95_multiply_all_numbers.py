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
  while True:
    choice = get_number("Enter a number: ")
    numbers.append(choice)
    if input("Add another number?(yes/no): ").lower().strip() == 'no':
      break
  if numbers:
    result = multiply(*numbers)
    number_str = " × ".join(map(str, numbers))
    print(f"{number_str} = {result}")
  else:
    print("No numbers entered")
  if input("Do you wanna continue (yes/no)?").lower().strip() == "no":
    break