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
      print("3. press 3 to substract numbers")
      print("4. press 4 to division numbers")
      print("5. press 5 to display the history")
      print("6. press 6 to stop the project")
      choice = int(input("Choose an action (1/2/3/4/5/6)"))
      
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
          print(f"Sum: {action_string} | action was added to memory")
        else:
          print("You must enter at least 2 numbers to start the process")
          
      elif choice == 2:
        a = get_numbers("enter a number: ")
        if len(a) > 1:
          formatted_numbers = [int(num) if num.is_integer() else num for num in a]
          result = 1
          for x in formatted_numbers:
            result *= x
          product = int(result) if result.is_integer() else result
          clean_line = ' × '.join(map(str, formatted_numbers))
          action_string = f"{clean_line} = {product}"
          memory['history'].append(action_string)
          print(f"Product: {action_string} | action was added to memory")
        else:
          print("You must enter at least 2 numbers to start the process")
          
      elif choice == 3:
        a = get_numbers("enter a number: ")
        if len(a) > 1:
          formatted_numbers = [int(num) if num.is_integer() else num for num in a]
          difference = formatted_numbers[0]
          for x in formatted_numbers[1:]:
            difference -= x
          result = int(difference) if difference.is_integer() else difference
          clean_line = ' - '.join(map(str, formatted_numbers))
          action_string = f"{clean_line} = {result}"
          memory['history'].append(action_string)
          print(f"Division: {action_string} | action was added to memory")
        else:
          print("You must enter at least 2 numbers to start the process")
          
      elif choice == 4:
        a = get_numbers("enter a number: ")
        if len(a) > 1:
          formatted_numbers = [int(num) if num.is_integer() else num for num in a]
          result = formatted_numbers[0]
          is_zero_division = False
          for x in formatted_numbers[1:]:
            if x == 0:
              print("\nError: Can not divide by zero! Operation aborted")
              is_zero_division = True
              break
            result /= x
          if not is_zero_division:
            quotient = int(result) if result.is_integer() else result
            clean_line = ' ÷ '.join(map(str, formatted_numbers))
            action_string = f"{clean_line} = {quotient}"
            memory['history'].append(action_string)
            print(f"Quotient: {action_string} | action was added to memory")
        else:
          print("You must enter at least 2 numbers to start the process")
          
      elif choice == 5:
        if memory['history']:
          print("\n---History of Actions---")
          for index, action in enumerate(memory['history'], 1):
            print(f"{index}. {action}")
        else:
          print("\nHistory is empty. No actions have been performed yet.\n")
          
      elif choice == 6:
        print("\nThe Project has been stopped, Bye!")
        break
      
      else:
        print("The wrong choice, Please select only actions 1 to 6")
        
    except ValueError:
      print("please write only numbers")
if __name__ == "__main__":
  main()