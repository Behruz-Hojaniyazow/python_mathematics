def collect_incubator_data():
  """function that analyzes the incubator's condition"""
  print("\n---Brama Incubator Monitoring System---")
  temps = []
  print("Type (stop) to finish")
  while len(temps) < 5:
    temp = input(f"Point {len(temps) + 1} Temp: ").strip()
    if temp.lower() == 'stop':
      break
    if temp:
      if temp.replace('.', '', 1).isdigit():
        temps.append(temp)
      else:
        print("(!)Please enter a enter a valid temperature")
    else:
      print("No Info entered")
  if not temps:
    print("No info collected, Process cancelled")
    return
  filename = 'incubator_cond.txt'
  try:
    with open(filename, 'w', encoding = 'utf-8') as f:
      f.write("\n".join(temps) + "\n")
    print(f"(!)[SUCCESS] Data saved to '{filename}' file")
  except Exception as e:
    print(f"An error occured, Problem writing to file - {e}")
if __name__ == "__main__":
  collect_incubator_data()