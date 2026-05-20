def file_reader():
  """Function that reads information about students"""
  
  filename = 'student_info.txt'
  
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = [line.strip() for line in file if line.strip()]
      if not lines:
        print("File is empty")
        return
      
      print("=" * 40)
      header = f"{"Student Name":<18} | {"Age":<6} | {"Score":<5}"
      print(header)
      print("-" * 40)
      for ind, line in enumerate(lines, start = 1):
        print(f"{ind}. {line}")
      print("=" * 40)
      if len(lines) > 1:
        print(f"{len(lines)} student records found!")
        
      else:
        print(f"{len(lines)} student record found")
  
  except FileNotFoundError:
    print(f"'{filename}' file not found, Please run the writer scrip first")
    
  except IOError as e:
    print(f"File Error - {e}")
    
  except Exception as e:
    print(f"Unexpected Error - {e}")
    
if __name__ == '__main__':
  file_reader()