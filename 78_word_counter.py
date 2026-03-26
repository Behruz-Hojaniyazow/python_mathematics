def word_count(fruits):
  fruits_info = {}
  for fruit in fruits:
    if fruit not in fruits_info:
      fruits_info[fruit] = 1
    elif fruit in fruits_info:
      fruits_info[fruit] += 1
  return fruits_info
all_products = []
while True:
  product = input("Which fruit do you need? ").strip().lower()
  all_products.append(product)
  answer = input("Do you need more fruit? (yes/no)")\
  .replace(" ", "").lower()

  if answer == 'no':
    break
num_of_fruit = word_count(all_products)
for fruit, quantity in num_of_fruit.items():
  if quantity == 1:
    print(f"There is {quantity} {fruit}")
  else:
    print(f"There are {quantity} {fruit}s")
    