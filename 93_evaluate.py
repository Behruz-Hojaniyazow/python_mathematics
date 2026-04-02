def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integer numbers")
def evaluate(names):
  """a function that evaluates students' scores"""
  if not names:
    return {}
  students = {}
  for name in names:
    score = get_number(f"Enter {name}'s' score: ")
    students[name] = (score)
  return students

students = []
while True:
  student = input("Enter a student's name or (type 'stop' to stop the project)").title()
  if student == "Stop":
    break
  if student.strip():
    students.append(student)
print("Okay, got it")
if students:
  info_students = evaluate(students)
  for name, score in info_students.items():
    print("-" * 30)
    print(f"{name} scored {score} points")
    print("-" * 30)
else:
  print("No information entered")