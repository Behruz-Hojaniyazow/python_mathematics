def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers, try again")
def filter_even_nums(*args):
  """a function that find the even numbers"""
  evens = []
  if not args:
    return []
  for num in args:
    if num % 2 == 0:
      evens.append(num)
  return evens
def main():
  numbers = []
  while True:
    print("Type <<stop>> to finish")
    number = get_number("Enter a number: ")
    numbers.append(number)
    if input("Will you add another number? (yes/no)").lower().strip() == 'no':
      break
  if numbers:
    even_numbers = filter_even_nums(*numbers)
    print("\n---These are the filtered even numbers---")
    beaty_evens = ", ".join(map(str, even_numbers))
    print(f"{beaty_evens}")
  else:
    print("No numbers entered")
if __name__ == "__main__":
  main()