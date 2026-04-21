def display_multification_table():
  """function that shows the multification table that you have entered"""
  filename = 'multification_table.txt'
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      if not lines:
        print("⚠️The file is empty")
        return
      filtered_lines = [line.strip() for line in lines if line.strip()]
      for index, line in enumerate(filtered_lines, start=1):
        print(f"[{index:02}] {line}")
          
  except FileNotFoundError:
    print(f"❌️Error: '{filename}' file not found, Please run the Writer script first")
  except Exception as e:
    print(f"❌️Unexpected Error - {e}")
    
if __name__ == '__main__':
  display_multification_table()