def uppercase_and_lowercase_letters(word):
  """a function that counts the uppercase and lowercase letters in the text"""
  lower_letters = 0
  upper_letters = 0

  for letter in word:
    if letter.isupper():
      upper_letters += 1
    elif letter.islower():
      lower_letters += 1
  return upper_letters, lower_letters
text = input("Enter text: ")
uppers, lowers = uppercase_and_lowercase_letters(text)
print("=" * 30)
print(f"Uppercase letters: {uppers}")
print("-" * 30)
print(f"Lowercase letters: {lowers}")
print("=" * 30)