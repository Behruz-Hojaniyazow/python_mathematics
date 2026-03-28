def find_the_longest_word(text):
  """a function that finds the longest word in the sentence"""
  words = text.split()
  chempion_word = ""
  for word in words:
    if len(word) > len(chempion_word):
      chempion_word = word
  return chempion_word, len(chempion_word)
sentence = input("Enter your sentence: ")
result, length = find_the_longest_word(sentence)
print(f"The longest word is {result.title()}, length: {length}")