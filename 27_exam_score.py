students_scores = {}
students_scores2 = []
while True:
  print("Type 'Stop' to stop the project")
  student = input("Enter the student's name ").title()
  score = float(input(f"enter {student}'s score: ")
  students_scores[student] = score
  students_scores2.append(score)
  lowest_score = min(students_scores2)
  highest_score = max(students_scores2)
  average_score = sum(students_scores2) / len(students_scores2)
  if student == 'Stop':
    print("project was stopped")
    break
for student, score in students_scores.items():
  print(f"{student} got {score}")
print(f"")