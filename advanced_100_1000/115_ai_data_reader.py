def read_and_sum_data():
  """function that reads the informations from the file"""
  name = input("Please, Enter your name: ")
  print(f"\n--- Welcome {name.title()} ---\n")
  filename = "ai_numbers.txt"
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      numbers = [float(line.strip()) for line in file if line.strip()]
      if not numbers:
        print("The file is empty")
      total_sum = sum(numbers)
      display_sum = int(total_sum) if total_sum.is_integer() else total_sum
      for index, num in enumerate(numbers, start=1):
        clean_num = int(num) if num.is_integer else num
        print(f"{index}. {clean_num}")
      print(f"Overall value: {display_sum}")
  except FileNotFoundError:
    print(f"The file '{filename}' was not found, Please run the writer first")
  except ValueError:
    print("Error: The file contains invalid numerical data")
  except Exception as e:
    print(f"An error occured - {e}")
if __name__ == '__main__':
  read_and_sum_data()