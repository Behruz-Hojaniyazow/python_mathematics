import math

def calculate_area(r):
  """function that calculates the area and perimeter of a circle"""
  if r < 0:
    raise ValueError("Radius can't be a negative!")
  return math.pi * math.pow(r, 2)
    
def calculate_circumference(r):
  if r < 0:
    raise ValueError("Radius can't be a negative!")
  return 2 * math.pi * r
    