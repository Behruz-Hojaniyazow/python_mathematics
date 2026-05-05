import sys

# Import modules
import geometry_2 as geo
import lucky_number as lucky
import travel_agent as ta
import efootball_pack as ep

def exit_app():
  """Exit the application gracefully"""
  print("\n👋🏼Thank you for using the Kryos project! GoodBye!")
  sys.exit()

def start_menu():
  """Display main menu and handle user navigation between features"""
  # We put the choices in the dictionary (Professional method) 
  menu_actions = {
    '1' : geo.main,
    '2' : lucky.find_ai_num,
    '3' : ta.main,
    '4' : ep.run_game,
    '5' : exit_app
  }
  
  while True:
    print("\n" + "=" * 40)
    print("--- 🚀 Kryos Multifunctional Software ---")
    print("=" * 40)
    print("1. Use geometry tools")
    print("2. Start lucky number game")
    print("3. Travel around the World")
    print("4. eFootBall pack opening")
    print("5. Stop the project")
    print("-" * 40)
    
    choice = input("Choose an action: ")
    
    if choice in menu_actions:
      # We get the function from the dictionary and run it
      menu_actions[choice]()
    else:
      print("\n❌️Error: Please choose a valid option (1-5")
      
if __name__ == "__main__":
  try:
    start_menu()
  except KeyboardInterrupt:
    #To prevent the program from giving an ugly error when pressing Ctrl+C
    exit_app()