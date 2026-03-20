users = ["admin", "engineer", "behruz_ai"]
attempts = 0
while attempts < 3:
  login = input("enter the username: ").strip().lower()
  if login in users:
    print(f"Acces Granted, Welcome,{login.title()}")
    break
  else:
    attempts += 1
    remaining = 3 - attempts
    print("Acces Denied! Incorrect username")
  
  if remaining > 0:
    print(f"You have {remaining} attempts left")
  else:
    blocked_user = users.pop()
    print("System Lockdown! Security breach detected.")
    print(f"User {blocked_user} has been removed from the system")
    print("please contact the adminstrator")