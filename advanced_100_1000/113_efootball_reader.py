def find_goats():
  """function that shows the players from the 'football_goats.txt' file"""
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}---")
  filename = "football_goats.txt"
  try:
    print("\n(!)These are the Football GOATs")
    with open(filename, 'r', encoding = 'utf-8') as file:
      players = [line.strip() for line in file.readlines() if line.strip()]
      if not players:
        print("The file is empty")
        return
      print(f"{len(players)} players were found")
      print("-" * 30)
      for index, player in enumerate(players, start=1):
        print(f"{index}. {player}")
      print("-" * 30)
  except FileNotFoundError:
    print(f"The file '{filename}' was not found, Please run the writer first")
  except Exception as e:
    print(f"Unexpected error occured - {e}")
if __name__ == "__main__":
  find_goats()