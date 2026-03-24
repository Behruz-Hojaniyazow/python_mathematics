def find_half(a):
  """a function thag finds the half of the given number"""
  num = a / 2
  return num
while True:
  try:
    number = float(input("Enter a number to find half of a number: "))
    break
  except ValueError:
    print("Please enter only numbers")
    
result = find_half(number)
print(f"The half of {number} is {result}")