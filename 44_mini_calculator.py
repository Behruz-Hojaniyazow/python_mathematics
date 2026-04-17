def get_numbers(prompt):
  """function that only accepts numbers from the user"""
  numbers = []
  print("Type 'stop' to finish")
  while True:
    try:
      num = input(prompt)
      if num.lower() == 'stop':
        break
      n = float(num)
      numbers.append(n)
    except ValueError:
      print("Please, Enter only numbers or type 'stop' to finish")
  return numbers
def main():
  memory = {"history" : []}
  while True:
    try:
      print("\n---Menu---")
      print("1. press 1 to add numbers")
      print("2. press 2 to multiply numbers")
      print("3. press 3 to stop the project")
      choice = int(input("Choose an action (1/2/3)"))
      user_input = input("Do you want to continue? (yes/no)")
      if user_input.lower() == 'no':
        break
      if choice == 1:
        a = get_numbers("enter a number: ")
        if len(a) > 1:
          total_sum = sum(a)
          display_sum = int(total_sum) if total_sum.is_integer() else total_sum
          formatted_numbers = [int(num) if num.is_integer() else num for num in a]
          clean_line = " + ".join(map(str, formatted_numbers))
          action_string = f"{clean_line} = {display_sum}"
          memory['history'].append(action_string)
          print(action_string)
          print(f"Result: {action_string}. action was added to memory")
        else:
          print("You must enter at least 2 numbers to start the process")
      elif choice == 2:
        a = float(input("enter the first number: "))
        result = a * b
        action_string = f"{a} × {b} = {result}"
        memory['history'].append(action_string)
        print(f"Result: {result}. action was added to memory")
      elif choice == 3:
        print("The project was stopped")
        print(memory)
        break
      else:
        print("The wrong choice, please choose only 1, 2, or 3")
    except ValueError:
      print("please write only numbers")
if __name__ == "__main__":
  main()