#even number from 0 to 20
number = 1
gathered = 0
while number <= 20:
  if number % 2 == 0:
    print(f"even number {number}")
    gathered += number
  number += 1
print(f"The sum of all even numbers {gathered}")