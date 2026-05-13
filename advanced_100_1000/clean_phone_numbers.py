phone_numbers = [' 63807476', ' 64277230  ', '63849125  ']
cleaned_numbers = list(
  map(lambda number: number.strip(), phone_numbers)
)
print(', '.join(cleaned_numbers))