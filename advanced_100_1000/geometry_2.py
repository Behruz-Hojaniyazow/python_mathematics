import geometry as geo

def get_numbers(prompt):
  """function that only accepts numbers from the user"""
  while True:
    try:
      val = float(input(prompt))
      if val < 0:
        print("❌️Radius must be a positive number!")
        continue
      return int(val) if val.is_integer() else val
    except ValueError:
      print("Error: Please enter only numbers")
      
def format_show(n):
  """making a number look nice: int if it's an int, .2f if it's a float"""
  return f"{n:.1f}" if isinstance(n, float) else n
      
def main():
  print("\n---KRYOS Geometry Tool---")
  
  num = get_numbers("Enter the radius of the circle: ")
  
  area = geo.calculate_area(num)
  length = geo.calculate_circumference(num)
  
  results = {
    "surface of a circle" : area,
    "length of a circle" : length
  }
  print("=" * 30)
  for key, value in results.items():
    print(f"{key.title()}: {format_show(value)}")
    print("-" * 30)
    
if __name__ == '__main__':
  main()