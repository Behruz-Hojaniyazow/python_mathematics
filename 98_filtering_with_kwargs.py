def get_number(prompt):
  """a function that only accpets integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers, try again")
def filter_by_value(**kwargs):
  """a function that filters the dic by value"""
  if not kwargs:
    return {}
  result = {}
  for item, value in kwargs.items():
    if value > 50:
      result[item] = value
  return result
def main():
  products = {}
  while True:
    print("type 'stop' to finish")
    product = input("Enter a product: ").title()
    if product == 'Stop':
      print("Bye")
      break
    value = get_number(f"Enter {product}'s price: ")
    products[product] = value
  if products:
    filtered = filter_by_value(**products)
    print("\n" + "~" * 30)
    print("These are the cleaned list")
    print("\n" + "~" * 30)
    print("-" * 30)
    for item, value in filtered.items():
      print(f"   - {item} | ${value}")
    print("-" * 30)
  else:
    print("No items entered")
if __name__ == "__main__":
  main()