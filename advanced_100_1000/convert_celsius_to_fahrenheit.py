celsius_temps = [12, 45, 34, 20]
fahrenheit = map(lambda temp: (temp * 1.8) + 32, celsius_temps)
clean_fahrenheit = [int(f) if isinstance(f, float) and f.is_integer() else round(f, 1) for f in fahrenheit]
print("Celcius ---> Fahrenheit")
print("-" * 30)
for c, f in zip(celsius_temps, clean_fahrenheit):
  print(f"{c}°C  --->  {f}°F")