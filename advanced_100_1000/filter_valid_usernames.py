names = ['anvar', 'behruz', 'mahmut', 'nuriya hojaniyazowa', 'ali']
formatted_names = map(lambda name: name.title(),
  filter(lambda name: len(name) > 5 and ' ' not in name,names))
print('\n'.join(formatted_names))