market = ["Arda", "Owen" ,"Messi" ,"Neymar" ,"Olise" ,"Vini"]
squad = []
n = 1
while n <= 3:
  player = input(f"{n} Which player do you need for your squad ? ").title()
  
  if player in market:
    squad.append(player)
    market.remove(player)
    print(f"\n{player} was added to the team")
    n += 1
  else:
    print(f"Unfortunately, {player} was sold out, or you entered the wrong name")
    
print("\nNow your squad became the best team in the world")
print(f"\n{squad}")