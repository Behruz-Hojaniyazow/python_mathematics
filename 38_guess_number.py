secret_number = 235.0

while True:
  user = float(input("guess a secret number: "))
  try:
    
    if user == secret_number:
      print("Congrats, you found the secret number")
      break
    
    elif user > secret_number:
      print("please enter a smaller number")
    else:
      print("please enter a larger number")
  except ValueError:
    print("please enter only numbers")