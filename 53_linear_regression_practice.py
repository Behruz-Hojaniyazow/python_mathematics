#y = wx + b
import random
print("\n---Linear Regression Practice Bot---")

w = random.randint(1, 10)
x = random.randint(1, 10)
b = random.randint(1, 10)
y_correct = w * x + b

print(f"\nGiven values: w = {w}, x = {x}, b = {b}")

while True:
  try:
    user = float(input("Which number is equal for 'y' ? "))
    
    if user == y_correct:
      print(f"\nCongrats, you found that {y_correct}")
      break
    else:
      print(f"Incorrect, please try again")
  except ValueError:
    print("please enter only numbers")
print(f"\n'y' equal to {y_correct}")
  