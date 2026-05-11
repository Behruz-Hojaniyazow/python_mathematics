names = ['behruz', 'anvar', 'mahmut']
mr_names = list(
  map(lambda name: f'Welcome Mr. {name.title()}!', names))
print('\n'.join(mr_names))