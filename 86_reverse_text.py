def reverse(text):
  """a function that returns the given string in reverse order"""
  return text[::-1]
while True:
  word = input("Enter a sentence: ")
  result = reverse(word)
  print(f"Reverse position = {result}")
  choice = input("Do you want to continue? (yes/no)").lower()
  if choice == 'no':
    break