#mashina zapchaslari

inventory = {"engine" : 5,
              "accumulator" : 2,
              "lidar" : 20,
              "tire" : 20
}

while True:
  
    print("\n<<<Menu>>>")
    print("press <1> to add details")
    print("press <2> to remove details")
    print("press <3> to show inventory")
    print("press <4> to stop the project")
    user = input("\nWhich one would you like me to do ?! (1/2/3/4)")
    
    if user == '1': #qoshish uchun 1
      part = input("Which part would you like to add? ").lower()
      try:
        amount = int(input(f"How many {part}s are you adding? "))
        if part in inventory:
          inventory[part] += amount
        else:
          inventory[part] = amount
        print(f"Update successful! Total {part}s: {inventory[part]}")
      except ValueError:
        print("Error, Please enter a valid number.")
      
    elif user == '2':
      part = input("Which part would you like to remove?").lower()
      
      if part in inventory:
        try:
          amount = int(input(f"How many {part}s to remove?(Available: {inventory[part]})"))
          if inventory[part] >= amount:
            inventory[part] -= amount
            print(f"The parts were removed successfully, ({inventory[part]} left in stock)")
        
          else:
            print(f"Action denied! Not enough {part}s in stock")
            print(f"You want {amount}, but there are only {inventory[part]} available to remove")
        except ValueError:
          print("Error, Please enter a valid number.")
      else:
          print(f"Error, The part {part} doesn't exist in your inventory")
          
        
    elif user == '3':
      print("\n--Here are the details of the cars--")
      for item, count in inventory.items():
        print(f"-{item.title()}: {count} units")
      
    elif user == '4':
      print("\nSystem shutting down. Goodbye")
      break
    else:
      print("You entered the wrong choice, please choose only (1/2/3/4)")
    
print("Congrats, your problem solved successfully Good luck")
print(f"Your cars are equipted with {inventory}")