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
  
  print('\n' + '=' * 43)
  print(f"{"Student name":<18} | {"Age":<6} | {"Score":<5}")
  print('-' * 43)
  
  if info_lists:
    for student in info_lists:
      print(f"{student['name'].title():<18} | {student['age']:<6} | {student['score']:<5}")
    print("=" * 43)
    
  else:
    print("\n(!) List is empty, Please add students first")
students = add_student()
show_students(students)