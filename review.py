def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("please enter only integer numbers")
def find_prime(number):
  """a function that identifies whether the number prime or composite"""
  if number <= 1:
    return "neither composite nor prime"
  for i in range(2, int(number * 0.5) + 1):
    if number % i == 0:
      return "composite"
  return "prime"
while True:
  amount = get_number("Enter a number: ")
  result = find_prime(amount)
  print(f"{amount} is a {result} number")
  if input("Shall we continue the project (yes/no)?").strip().lower() == 'no':
    print("Bye, The project was ended")
    break
  def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Iltimos, faqat butun son kiriting!")

def evaluate(names):
    # Agar ro'yxat bo'sh bo'lsa, bo'sh lug'at qaytargan ma'qul
    if not names:
        return {}
    
    students_data = {}
    # pop() o'rniga oddiy for ishlatamiz (tartib saqlanadi)
    for name in names:
        score = get_number(f"Enter {name}'s score: ")
        students_data[name] = score
    return students_data

# Asosiy qism
students_list = []
while True:
    student = input("Enter a student's name or (type 'stop' to stop): ").title()
    
    if student == "Stop":
        break
    
    # Bo'sh ism kiritilishini oldini olish
    if student.strip():
        students_list.append(student)

print("Bye")

if students_list:
    info_students = evaluate(students_list)
    print("-" * 30)
    for name, score in info_students.items():
        print(f"{name} student got {score} score")
else:
    print("No information entered")
