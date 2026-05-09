family_members = ['behruz', 'anvar', 'mahmut', 'nuriya', 'zamira']
filtered = list(
  filter(lambda x: len(x) > 5,
  map(lambda x: x.title(), family_members)))
clean_names = ', '.join(filtered)
print(clean_names)