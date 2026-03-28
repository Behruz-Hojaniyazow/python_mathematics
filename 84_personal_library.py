def personal_library(name_of_book, year_of_public, author="Unknown"):
  """a function that collects informations about the book"""
  info_book = {
    "name_of_book" : name_of_book,
    "author" : author,
    "year_of_public" : year_of_public
  }
  return info_book
books = []
print("---Program for adding books to the library---")
while True:
  name = input("Enter the book's name: ")
  year = input(f"Enter the {name.title()} book's publication year: ")
  author_input = input(f"Enter the {name.title()} book's author: (if you don't know leave it alone)")
  if author_input == "":
    new_book = personal_library(name, year)
  else:
    new_book = personal_library(name, year, author_input)
  books.append(new_book)
  answer = input("Do you want to add more books? (yes/no)").lower()
  if answer == 'no':
    break
print("=" * 30)
print("\nBooks in our library")
print("=" * 30)
for book in books:
  print(f"Name of the book is |  {book['name_of_book'].title()},\nPublished year | {book['year_of_public']},\nThe author of the book is |  {book['author'].title()}")
  print("-" * 30)