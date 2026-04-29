import arithmetic as art

def get_numbers(prompt):
  """function that only accepts numbers from fhe user"""
  while True:
    try:
      val = float(input(prompt))
      return int(val) if val.is_integer() else val
    except ValueError:
      print("❌️Error: Please enter only numbers")
      
def format_show(n):
  """making a number look nice: int if it's an int, .2f if it's a float"""
  if isinstance(n, float):
    return f"{n:.1f}"
  return n
      
def main():
  print("---Arithmetic Operations Program---")
  num_1 = get_numbers("Enter the 1st number: ")
  num_2 = get_numbers("Enter the 2nd number: ")
  
  results = {
    "+" : art.addition(num_1, num_2),
    "-" : art.subtraction(num_1, num_2),
    "×" : art.multiplication(num_1, num_2)
  }
  print("\n---Results---\n")
  for sign, value in results.items():
    n1_f = format_show(num_1)
    n2_f = format_show(num_2)
    res_f = format_show(value)
    print(f"{n1_f} {sign} {n2_f} = {res_f}")
    
if __name__ == "__main__":
  main()