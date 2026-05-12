products = {
  'phone' : 340,
  'notebook' : 1000,
  'earphone' : 60,
  'watch' : 50,
  'laptop' : 200,
  'charger' : 30
}
expensive_products = dict(
  filter(lambda item: item[1] > 100, products.items())
)
for item, price in expensive_products.items():
  print(f" -  {item.title()} costs ${price}!")