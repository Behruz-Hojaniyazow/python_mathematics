MIN_SAFE_TEMP = 37
MAX_SAFE_TEMP = 38.5
#_1 creatin a function
def check_incubator_status():
  #_writing docstring to understand the function easily
  """function that reads the info from the file 'temperature_cond.txt' file"""
  print("\n---Welcome---\n")
  #_entering the filename that you created
  filename = 'incubator_cond.txt'
  #_using try...except to ensure the mistakes
  try:
    with open(filename, 'r' ,encoding = 'utf-8') as file:
      data = [float(line.strip()) for line in file if line.strip()]
      if not data:
        print("No Data found in incubator log")
        return
      print("\n---Incubator Status Report---\n")
      print("=" * 30)
      danger_found = False
      for i, temp in enumerate(data, start=1):
        status = "NORMAL"
        #_We check each point separately
        if temp > MAX_SAFE_TEMP:
          status = "!!! DANGER: TOO HOT !!!"
          danger_found = True
        elif temp < MIN_SAFE_TEMP:
          status = "!!! DANGER: TOO COLD !!!"
          danger_found = True
        #_with .is_integer we are gonne display the result
        display_temp = int(temp) if temp.is_integer else temperature_cond
        print(f"Sensor {i}: {display_temp}°C -> {status}")
        if danger_found:
          print("\nWARNING: Immediate action required for Brama chicks")
        else:
          print("\nALL systems normal, Optimal environment")
          
  except FileNotFoundError:
    print(f"The file '{filename}' was not found, Please run the Writer first")
  except ValueError:
    print("Error: The file contains invalid numerical data")
  except Exception as e:
    print(f"An error occured.- {e}")
if __name__ == "__main__":
  check_incubator_status()