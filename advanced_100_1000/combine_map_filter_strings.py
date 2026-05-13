names = ['anvar', 'zamira', 'behruz', 'mahmut', 'nuriya']
necessary_names = list(
  map(lambda name: name.upper(),
  filter(lambda name: len(name) > 5, names)
  )
)
print('\n'.join(necessary_names))