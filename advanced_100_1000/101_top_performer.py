def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers")
def find_top_performer(name, **kwargs):
  """a function that finds the top performer"""
  print("~" * 30)
  print(f"\n===Student {name.title()}===")
  print("~" * 30)
  if not kwargs:
    return "No information entered"
  max_score = max(kwargs.values())
  top_scores = {subject: score for subject, score in kwargs.items() if score == max_score}
  return max_score, top_scores
def main():
  user_name = input("Enter your name: ")
  print(f"\n---Welcome {user_name.title()} enter your subject information---")
  all_subjects = {}
  while True:
    print("Type 'stop' to finish")
    key = input("Enter a subject: ")
    if key.lower() == 'stop':
      break
    value = get_number(f"How much score did you get from {value}? ")
    all_subjects[key] = value
  if all_subjects:
    result = find_top_performer(user_name, **all_subjects)
    print("These are your top performances")
    print("=" * 30)
    for subj, score in result.items():
      print(f" -  {subj} | {score}")
      print("=" * 30)
  else:
    print("No info entered")
if __name__ == "__main__":
  main()