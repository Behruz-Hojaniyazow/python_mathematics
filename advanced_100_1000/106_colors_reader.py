def colors_reader():
  """function that reads the info from 'colors.txt' file"""
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}!---")
  filename = 'colors.txt'
  try:
    with open (filename, 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      if lines:
        print(f"\n{len(lines)} colors were found from the '{filename}' file")
        for index, line in enumerate(lines, start=1):
          clean_line = line.upper().strip()
          print(f"{index}. {clean_line}")
      else:
        print("The file was empty")
  except FileNotFoundError:
    print(f"The file {filename} was not created, Please run the Writer first")
if __name__ == "__main__":
  colors_reader()