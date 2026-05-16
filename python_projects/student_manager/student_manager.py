def get_numbers(prompt):
  """function that only accepts numbers from the user"""
  while True:
    try:
      val = float(input(prompt))
      return int(val) if val.is_integer() else val
    except ValueError:
      print("(!) Please write only numbers")

def add_student():
  """Collects student data (name, age, grade) and returns it in a list format"""
  
  students_list = []
  order = 1
  
  print("Start entering students. To stop, type 'stop' instead of the name.")
  
  while True:
    print(f"\n{order}-Enter a student information!")
    name = input("Name: (or 'stop): ").strip()
    
    if name.lower() == 'stop':
      print("Data collection has stopped")
      break
    
    age = get_numbers("Age: ")
    score = get_numbers("Score: ")
    
    student = {
      'name' : name,
      'age' : age,
      'score' : score
    }
    
    students_list.append(student)
    order += 1
  return students_list
  
def show_students(info_lists):
  """Outputs name, age, and grades to the console in a nice table format"""
  if not info_lists:
    print("(!) Student list is empty")
    return
  
  print('\n' + '=' * 43)
  print(f"{"Student name":<18} | {"Age":<6} | {"Score":<5}")
  print('-' * 43)
  
  for student in info_lists:
    print(
      f"{student['name'].title():<18} | "
      f"{student['age']:<6} | "
      f"{student['score']:<5}"
      )
    print("=" * 43)
    
def search_students(students):
  """function that seraches a student from the list"""
  
  if not students:
    print("(!) Student list is empty")
    return
  
  while True:
    print("Type (stop) to finish")
    user_input = input("\nEnter the name of the student you are looking for: ").strip()
    
    if user_input.lower() == 'stop':
      print("\nProgram stopped, Thanks!")
      break
      
    found = False
      
    for student in students:
      if student['name'].lower() == user_input.lower():
        print("\nYes! This student is in the Class Regsiter")
        print(f"Name {student['name'].title()} | Age {student['age']} | Score {student['score']}")
        found = True
        break
    if not found:
      print(f"\nUnfortunately! a student named {user_input} is not in Class Register!")