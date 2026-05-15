python_users = [
  {'name' : 'behruz', 'active' : True},
  {'name' : 'mahmut', 'active' : False},
  {'name' : 'sariq dev', 'active' : True}
]
active_users = [
  user['name'].title()
  for user in python_users
  if user['active']
]
print('\n'.join(active_users))