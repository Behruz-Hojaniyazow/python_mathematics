import hashlib

def get_hashed_input(raw_password):
  """convert the entered password to a SHA-256 hash"""
  return hashlib.sha256(raw_password.encode()).hexdigest()
  
def password_check():
  """function that checks the given password"""
  filename = "secret_password.txt"
  print("\n--- KRYOS SHIELD: Control System ---\n")
  
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      vault_data = file.readlines()
      while True:
        user_input = input("Enter the password: type 'stop' to leave: ").strip()
      
        if user_input.lower() == 'stop':
          break
        #_hashing the entered password
        input_hash = get_hashed_input(user_input)
        #_searching for the hash from each line in the file
        found = False
        for line in vault_data:
          if input_hash in line:
            found = True
            break
          
        if found:
          print("✅️SUCCESS: Welcome to the project")
        else:
          print("❌️Error: The Password is wrong, Try again")
  except FileNotFoundError:
    print(f"No file found called {filename}, Please run the Writer first")
  except Exception as e:
    print(f"An error occured - {e}")
    
if __name__ == '__main__':
  password_check()