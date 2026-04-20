#workers and their monthly funds
workers = {
           "alex" : 800,
           "john" : 870,
           "david" : 1200,
           "scott" : 950,
           "kendy" : 1100
}
#we are gonna add the workers into another (dictionary) who earns more than 1000
wealthy_w = {}
for name, salary in workers.items():
  if salary > 1000:
    wealthy_w[name] = salary
print("💸" *30)
print(f"Wealthy workers {wealthy_w}")