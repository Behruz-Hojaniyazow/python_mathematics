#This is the old version
import math
import numpy as np
from sympy import symbols, Eq, solve
def yechuvchi():
	print("--- Kwadrat tenglama yechuvchi ---")
	a = float(input("a-ni kiriting"))
	b = float(input("b-ni kiriting"))
	c = float(input("c-ni kiriting"))
	D = (b**2) - 4 * a * c
	print(f"\nDiskriminant: D={D}")
	if D >= 0:
		sqrt_d = math.sqrt(d)
		x1 = (-b + sqrt_d) / (2 * a)
		x2 = (-b - sqrt_d) / (2 * a)
		print(f"Tenglama javoblari: x1 = {x1}, x2 = {x2}")
	else:
		print("Tenglamaning javobi yoq chunki (D < 0)")
#Numpy usulida
	np_javob = np.roots([a, b, c])
	print(f"NumPy usulida: {np_javob}")
yechuvchi()




#This is the new version of quadratic equation solver
import math
import numpy as np
def solve_equation(a, b, c):
  """a function that calculates the equation"""
  d = (b)**2 - 4 * a * c
  if d < 0:
    return d, None, None
  sqrt_d = math.sqrt(d)
  x1 = (-b + sqrt_d) / (2 * a)
  x2 = (-b - sqrt_d) / (2 * a)
  return d, x1, x2
def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers")
while True:
  print("---Quadratic equation solver---")
  a = get_number("a = ")
  if a == 0:
    print("If a equal to 0, this is not a quadratic equation")
    continue
  b = get_number("b = ")
  c = get_number("c = ")
  d, x1, x2 = solve_equation(a,b,c)
  print(f"\nDiscriminant: D = {d}")
  if d > 0:
    print(f"Equation answers: x1 = {x1:.2f}, x2 = {x2:.2f}")
  elif d == 0:
    print(f"Same answers: x = {x1:.2f}")
  else:
    print("There are no real roots (d<0)")
  #nice formatting of numpy output
  np_result = np.roots([a,b,c])
  #we convert each root to text with 2 digits of precision
  beautiful_np = ", ".join([f"{root:.2f}" for root in np_result])
  print(f"Numpy check: {beautiful_np}")
  if input("Do you have another quadratic equation to solve? (yes/no)").lower() != 'yes':
    print("Bye")
    break