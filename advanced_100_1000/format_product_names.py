products = ['iphone', 'samsung', 'redmi']
clean_products = list(
  map(lambda item: f'{item.title()} Product', products)
)
print('\n'.join(clean_products))