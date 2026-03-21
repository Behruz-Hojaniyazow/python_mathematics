books = {"Python" : 3,
        "Math" : 5,
        "Physics" : 2,
        "Geometry" : 0,
        "Literature" : 0,
        "Chemistry" : 4
}
while True:
  reader = input("Which book do you need? ").strip().title()
  if reader in books and books[reader] > 0:
    books[reader] -= 1
    print(f"Your order {reader.title()} book will be ready in 5 minutes")
  elif reader in books and books[reader] == 0:
    print(f"Sorry, {reader} book is out of stock")
  elif reader == 'Return':
    returned_b = input("Which book are you going to you return?")/
    .strip().title()
    value = int(input(f"How many {returned_b} book are you going to return? ")
    if returned_b in books:
      books[returned_b] += value
      print(f"{returned_b} book added to the dict")
    else:
      books[returned_b] = value
      print(f"{return_b} added to the dict")
  elif reader == 'Bye':
    break
print(f"\nThank you for using our library")
print(f"\n---Current library--- ")
print(f"books")
      