def filter_dict(**kwargs):
  """a function that filters the dict"""
  if kwargs:
    clean_data = {}
    for key, value in kwargs.items():
      if isinstance(value, (int, float))
      clean_data[key] = value
  return clean_data
def main():
  filtered_data = {}
  while True:
    print("type 'stop' to finish")
    kwargs_key = input("Type of information? ")
    if kwargs_key.lower() == 'stop':
    break
    kwargs_value = input(f"Enter the value of {kwargs_key}: ")
    filtered_data[kwargs_key] = kwargs_value
  if filtered_data:
    result = filter_dict(**filtered_data)
    print("\n" + "~" * 30)
    for key, value in result.items():
      print(f"  - {key} | {value}")
    print("~" * 30)
  else:
    print("No information entered")
if __name__ == "__main__":
  main()