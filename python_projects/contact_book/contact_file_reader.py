def file_reader():
  """Function that reads contact information from the file"""
  
  filename = 'contacts_info.txt'
  
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = [line.strip() for line in file if line.strip()]
      
      if not lines:
        print("\nFile is empty")
        return
      header = f"{"Name":<18} | {"Phone Number":<20}"
      print("=" * 40)
      print(header)
      print("-" * 40)
      for ind, line in enumerate(lines, start = 1):
        print(f"{ind}. {line}")
      print("=" * 40)
      if len(lines) > 1:
        print(f"{len(lines)} contacts were found")
      else:
        print(f"{len(lines)} contact was found")
      
  except FileNotFoundError:
    print(f"\n'{filename}' file not found, Please run the writer scrip first")
  
  except IOError as e:
    print(f"\nFile Error - {e}")
    
  except Exception as e:
    print(f"\nUnexpected Error occured - {e}")
    
if __name__ == '__main__':
  file_reader()