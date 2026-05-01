import random as r

def get_random_destination(destinations) -> str:
  """Selects a random travel route from the list"""
  if destinations:
    return r.choice(destinations)
  return "No travel directions shown!"
  
def get_sorted_destinations(destinations: list) -> list:
  """Sorts directions alphabetically"""
  if destinations:
    return sorted(destinations)
  return "No country found"