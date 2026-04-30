import lucky_number as ln

def start_menu():
  print("---🌟 Kryos Multifunctional Software ---")
  print("1. Starting the game..")
  print("2. Exit")
  
  choice = input("Choose an action: ")
  if choice == '1':
    ln.find_ai_num()
    
  elif choice == '2':
    print("GoodBye 👋🏼")
  
  else:
    print("⚠️ The wrong choice")
    
if __name__ == "__main__":
  start_menu()
    