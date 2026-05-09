names = ['behruz', 'mahmut', 'anvar']
upper_names = list(map(lambda x: x.title(), names))
result = ', '.join(upper_names)
print(result)