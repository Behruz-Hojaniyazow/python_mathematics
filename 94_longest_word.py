def analyze_text(texts):
  """a function that finds the longest word in the list"""
  longest_word = ""
  longest_length = 0
  for text in texts:
    count = 0
    for letter in text:
      count += 1
    print(f"\n{text} has {count} letters")
    if count > longest_length:
      longest_word = text
      longest_length = count
  return longest_word, longest_length
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
    print("=" * 30)
    print(f"The longest word is {word}")
    print("-" * 30)
    print(f"{word} has {length} letters")
    print("=" * 30)
  else:
    print("No information entered")
if __name__ == "__main__":
  main()