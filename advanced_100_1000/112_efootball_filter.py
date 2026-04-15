def get_best_players():
  """function that finds the best football players"""
  player_list = []
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}, Enter the best five players---\n")
  print("Type 'stop' to finish")
  while len(player_list) < 5:
    player = input("Enter a player: ").strip()
    if player.lower() == 'stop':
      break
    if player:
      player_list.append(player)
  if player_list:
    r_players = [player for player in player_list if player.lower().startswith('r')]
    if r_players:
      print("\n(!)These are the football GOATs")
      filename = "football_goats.txt"
      try:
        with open(filename, 'a', encoding = 'utf-8') as file:
          for player in r_players:
            file.write(f"{player.title()}\n")
            print("-" * 30)
            print(f"- {player.title()}")
          print("-" * 30)
        print(f"\n{len(r_players)} players were saved to the '{filename}' file")
      except Exception as e:
        print(f"An error occured: Problem writing to file - {e}")
    else:
      print("No Football goats were entered, File was not created")
  else:
    print("No info was entered, File was not created")
if __name__ == "__main__":
  get_best_players()