def infos(name, *args, **kwargs):
  """a function that shows you how to order args and kwargs"""
  print(f"\n===== REPORT: {name.upper()}=====")
  if args:
    print("Informations that you entered as an (*args):")
    for i, value in enumerate(args, 1):
      print(f"  - {i} {value}")
  if kwargs:
    print("\nInformations that you entered as a (**kwargs):")
    for key, value in kwargs.items():
      print(f"  ~ {key.capitalize()} - {value.title()}")
#1majburiy ism
user_name = input("Enter your name: ").title()
#2adding infos for args as a list
user_args = []
print("\n---Optional Information---")
while True:
  print("type 'stop' to finish")
  extra = input("Enter an additional information: ").title()
  if extra == 'Stop':
    break
  user_args.append(extra)
#3adding infos for kwargs as a dict
user_kwargs = {}
print("\n---Informations with keys, for example (city - newyork)---")
while True:
  print("type 'stop' to finish")
  key = input("Type of information? ")
  if key.lower() == 'stop':
    break
  value = input(f"Enter the value of {key}: ")
  user_kwargs[key] = value
#funksiyani chaqirish (MAIN PART)
infos(user_name, *user_args, **user_kwargs)