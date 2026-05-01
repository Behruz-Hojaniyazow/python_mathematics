import geometry_2 as geo
import lucky_number as ln
import travel_agent as ta
import sys

def exit_app():
  print("\n👋🏼Thank you for using the Kryos project! GoodBye!")
  sys.exit()

def start_menu():
  """main menu and feature management"""
  # We put the choices in the dictionary (Professional method) 
  menu_actions = {
    '1' : geo.main,
    '2' : ln.find_ai_num,
    '3' : ta.main,
    '4' : exit_app
  }
  
  while True:
    print("\n" + "=" * 40)
    print("--- 🚀 Kryos Multifunctional Sowftware ---")
    print("=" * 40)
    print("1. Use geometry tools")
    print("2. Start lucky number game")
    print("3. Travel around the World")
    print("4. Stop the project")
    print("-" * 40)
    
    choice = input("Choose an action: ")
    
    if choice in menu_actions:
      # Lug'atdan funksiyani olib, uni ishga tushiramiz
      menu_actions[choice]()
    else:
      print("\n❌️Error: Wrong choice! Please enter 1, 2 or 3")
      
if __name__ == "__main__":
  try:
    start_menu()
  except KeyboardInterrupt:
    #To prevent the program from giving an ugly error when pressing Ctrl+C
    exit_app()