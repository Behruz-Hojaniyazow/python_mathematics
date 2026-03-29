def palendrom(words):
  palendrom_list = []
  """a function that checks if the word is palendrom"""
  for text in words:
    if text == text[::-1]:
      palendrom_list.append(text)
  return palendrom_list
palendroms = []
while True:
  word = input("Enter a word: ")\
  .strip().lower()
  palendroms.append(word)
  answer = input("Do you need more words? (yes/no)")\
  .replace(" "," ").lower()
  if answer == 'no':
    break
result = palendrom(palendroms)
print(f"These are the palendroms {result}")