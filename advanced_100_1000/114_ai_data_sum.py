def collect_and_save_data():
  """function that writes the given numbers to the file"""
  name = input("Enter your name: ")
  print(f"\n---Welcome {name.title()}!---")
  print("\n--- AI Data Collection System ---")
  print("\n(!)Enter 10 numbers\n")
  numbers = []
  print("Type 'stop' to finish")
  while len(numbers) < 10:
    number = input("Enter a number: ")
    if number.lower() == 'stop':
      break
    if number:
      if number.replace('.', '', 1).isdigit():
        numbers.append(number)
      else:
        print("(!) Please enter a valid numerical value")
    else:
      print("(!) Please enter a number, No info entered")
  if not numbers:
    print("No data collected, Process  cancelled")
    return
  filename = 'ai_numbers.txt'
  try:
    with open(filename, 'w', encoding = 'utf-8') as file:
      file.write("\n".join(numbers) + "\n")
    print(f"{len(numbers)} numbers were saved to the : '{filename}' file")
  except Exception as e:
    print(f"An error occured, Promlem writing to file - {e}")
if __name__ == '__main__':
  collect_and_save_data()