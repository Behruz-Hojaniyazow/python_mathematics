students_scores = {}
n = 1
while True:
  try:
    student = input(f"{n} enter the  student's name: ")
    score = int(input(f"How much did {student.title()} get ? "))
    repeating = input("Would you like to add more information ? (yes/no)")
    students_scores[student] = score
    n+=1
    if repeating.lower().startswith('n'):
      break
  except ValueError:
    print("please write only numbers")
for student, score in students_scores.items():
  print(f"{student.title()} got {score}")