names = ['behruz', 'mahmut', 'nuriya']
prefix_names = [f"{ind}. {name.title()}" for ind, name in enumerate(names, start=1)]
for name in prefix_names:
  print(name)