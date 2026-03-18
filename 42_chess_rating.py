rating = {"Behruz" : 1500,
          "Adyl" : 1500
}

while True:
  winner = input("Who won the match ? \n 'Behruz' or 'Adyl' \n(type 'stop' to leave)").title()
  if winner == 'Stop':
    break
  if winner == 'Behruz':
    rating['Behruz'] += 15
    rating['Adyl'] -= 15
    print(f"Keep up the good work {winner.title()}")
  elif winner == 'Adyl':
    rating['Adyl'] += 15
    rating['Behruz'] -= 15
    print(f"Your opponent {winner} is not bad wake up")
    
  else:
    print("You entered the wrong information, Try again")
  if rating['Behruz'] >= 1600:
    print("Congrats, You have reached 1600 elo rating")
    break
  if rating['Adyl'] >= 1600:
    print("Unfortunately, your opponent has reached 1600 elo rating")
    break
    