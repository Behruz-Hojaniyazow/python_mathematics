def incubator_alert():
  """function that analyzes the incubator's condition"""
  print("\n---Welcome! Enter the temperatures of five days---")
  temperatures = []
  print("Type (stop) to finish")
  while len(temperatures) < 5:
    temperature = input("Enter the temperature: ")
    if temperature.lower() == 'stop':
      break
    if temperature:
      if temperature.replace('.', '', 1).isdigit():
        temperatures.append(temperature)
      else:
        print("(!)Please enter a numerical number")
    else:
      print("No Info entered")
  if not temperatures:
    print("No info collected, Process cancelled")
    return
  filename = 'incubator_cond.txt'
  try:
    with open(filename, 'w', encoding = 'utf-8') as f:
      f.write("\n".join(temperatures) + "\n")
    print(f"(!){len(temperatures)} incubator temperatures were saved successfully to the '{filename}' file")
  except Exception as e:
    print(f"An error occured, Problem writing to file - {e}")
if __name__ == "__main__":
  incubator_alert()