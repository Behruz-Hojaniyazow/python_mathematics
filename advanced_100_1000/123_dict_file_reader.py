def dict_file():
  """function that shows the data in the file"""
  filename = "neoplan_clients.txt"
  
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = [line.strip() for line in file if line.strip()]
      if not lines:
        print("The file is empty")
        return
      for line in lines:
        print(f"{line}")
      print(f"{len(lines)} clients were found")
  except FileNotFoundError:
    print(f"Error: {filename} file not found, Please run the writer script first")
  except IOError as e:
    print(f"File Error - {e}")
  except Exception as e:
    print(f"Unexpected Error - {e}")
if __name__ == '__main__':
  dict_file()