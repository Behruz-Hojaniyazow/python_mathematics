import math
def get_number(string):
  while True:
    try:
      return float(input(string))
    except ValueError:
      print("Please, enter only numbers")
def circle_area():
  """a function that accepts a given number and calculates the area of the a circle"""
  r = get_number("What is the radius: ")
  s = math.pi * r**2
  print(f"The are of the circle is equal to {s}")
circle_area()