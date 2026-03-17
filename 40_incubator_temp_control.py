current_temp = float(input("What is the current temperature ? "))
while current_temp < 37.8:
  current_temp += 0.5
  print(f"Heating... Current {current_temp:.1f}")
  
while current_temp > 38.3:
  current_temp -= 0.5
  print(f"Cooling... Current {current_temp:.1f}")
  
print("ideal temperature reached")
print(f"\nYour incubator has reached {current_temp:.1f}")