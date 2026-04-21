def get_numbers(prompt):
  """function that only accepts mumbers from the user"""
  while True:
    try:
      val = float(input(prompt))
      return int(val) if val.is_integer() else val
    except ValueError:
      print("Please, Enter only numbers")
      
def multification():
  """function that multiplies the given number"""
  filename = 'multification_table.txt'
  number = get_numbers("What number multification table do you need? ")
  try:
    with open(filename, 'a', encoding = 'utf-8') as f:
      f.write(f"That is the multification table for number {number}\n\n")
      
      for i in range(1, 11):
        result = number * i
        clean_res = int(result) if isinstance(result, float) and result.is_integer() else result
        
        line = f"{number} × {i} = {clean_res}\n"
        f.write(line)
      print(f"This multification table were saved successfully to the '{filename}' file")
      
  except Exception as e:
    print(f"An error occured = {e}")
  
if __name__ == '__main__':
  multification()