import hashlib
import getpass #for not seing the password while entering

def save_password_shield():
  """function that accepts the secret password to the file"""
  print("=" * 30)
  print("       KRYOS PASSWORD SHIELD")
  print("=" * 30)
  
  service = input("Enter service name(e.g. Gmail): ").strip()
  #entering the password hidely and safely
  while True:
    password = getpass.getpass("Enter secure password: ")
    #password must be at least 8 characters
    if len(password) < 8:
      print("(!) Weak password, Must be at least 8 characters")
      continue
    break
  # Hashing: We make the password "unrecognizable"
  # The SHA-256 algorithm makes the password irreversible
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  filename = "secret_password.txt"
  try:
    with open(filename, 'a', encoding = 'utf-8') as f:
      f.write(f"Service: {service} | Vault_Key: {hashed_password}\n")
    print(f"[SUCCESS]: Password for {service} secured in the vault!")
  except Exception as e:
    print(f"An error occured - {e}")
if __name__ == "__main__":
  save_password_shield()