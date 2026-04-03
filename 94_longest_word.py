def analyze_text(texts):
  """a function that finds the longest word in the list"""
  longest_length = 0
  longest_words = []
  for text in texts:
    count = 0
    for letter in text:
      count += 1
    print(f"\n{text} has {count} letters")
    if count > longest_length:
      longest_length = count
      longest_words = [text]
    elif count == longest_length and count != 0:
      longest_words.append(text)
  return longest_words, longest_length
def main():
  words = []
  while True:
    print("type (stop) to stop the project")
    word = input("Enter a word: ").title().strip()
    if word == "Stop":
      break
    if word:
      words.append(word)
  if words:
    word, length = analyze_text(words)
    if len(word) > 1:
      print(f"\nThe longest words have {length} letters")
      print("These are the longest texts")
      print("=" * 30)
      for w in word:
        print(f"{w} | {length} letter")
        print("-" * 30)
    else:
      name = word[0]
      print(f"\nThe longest word has {length} letters")
      print("This is the only longest text")
      print("="  * 30)
      print(f"{name} | {length} letter")
      print("-"  * 30)
  else:
    print("No information entered")
if __name__ == "__main__":
  main()