import random as r

def get_number(prompt):
  """function that only accepts numbers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("❌️Error: Please enter only integer numbers")
      
def find_ai_num():
  """function that finds the number that ai thinks"""
  ai_num = r.randint(1, 100)
  attempts = 0
  
  print("\n--- 🎯 Kryos Lucky Number Game---")
  print("I thought of a number from 0 to 100, Can you find it?")
  
  while True:
    attempts += 1
    user_num = get_number(f"Attempt {attempts}: Enter a number: ")
    if user_num > ai_num:
      print("📉 Please enter a smaller number...")
    elif user_num < ai_num:
      print("📈 Please enter a larger number")
    else:
      print(f"️✅️ Congrats! You found it in {attempts} tries!")
      break
    
if __name__ == "__main__":
  find_ai_num()