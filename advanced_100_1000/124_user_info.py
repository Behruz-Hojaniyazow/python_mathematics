def creating_file():
  """function that creates a file"""
  filename = "original.txt"
  print("\n---Enter info about yourself---\n")
  user_info = []
  full_name = input("Enter your full name: ").strip()
  if full_name:
    user_info.append(full_name)
  born_year = input("When were you born: ").strip()
  if born_year:
    user_info.append(born_year)
  country = input("Where were you born: ").strip()
  if country:
    user_info.append(country)
  if user_info:
    try:
      with open(filename, 'w', encoding = 'utf-8') as f:
        for info in user_info:
          f.write(f"{info.title()}\n")
      print(f"\nUser info saved successfully to the {filename} file")
    except Exception as e:
      print(f"An error occured - {e}")
  else:
    print("File was not created, because the list is empty")
if __name__ == '__main__':
  creating_file()