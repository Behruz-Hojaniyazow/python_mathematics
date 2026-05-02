import random as

def get_mix_list(items: list) -> list:
  """Return a shuffled copy of the input list."""
  new_list = list(items)
  random.shuffle(new_list)
  return new_list