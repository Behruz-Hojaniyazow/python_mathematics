import os

def cloning_file(input_path = 'original.txt', output_path = 'copy.txt'):
  """reads data from a file, formats it, and copies it to a new file"""
  # 1. checking if the file exists (Check before try)
  if not os.path.exists(input_path):
    print(f"Error: '{input_path}' not found")
    return
  
  try:
    # 2. Reading and processing information
    with open(input_path, 'r', encoding = 'utf-8') as source:
      lines = [line.strip() for line in source if line.strip()]
      # We clean up the non-empty rows and list them
      if not lines:
        print(f"Warning: '{input_path}  file is empty")
        return
      
      # 3. Ma'lumotni yangi faylga yozish
      
      with open(output_path, 'w', encoding = 'utf - 8') as destination:
        for index, line in enumerate(lines, start = 1):
          # Simultaneously output to the console and write to a file
          print(f"{index}. {line}")
          destination.write(f"{line}\n")
          
      print(f"{len(lines)} user info saved successfully to the '{output_path}' file")
      
  except IOError as e:
    # Tizim darajasidagi xatolar uchun (masalan, ruxsat yo'qligi)
    print(f"An unexpected error occured while working with the file")
if __name__ == '__main__':
  cloning_file()