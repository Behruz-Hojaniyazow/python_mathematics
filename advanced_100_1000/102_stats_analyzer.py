def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers, try again")
def analyze_stats(**kwargs):
  """a function that analyzes the given stats"""
  if not kwargs:
    return "No information entered"
  max_score = max(kwargs.values())
  min_score = min(kwargs.values())
  top_subjects = [sub.capitalize() for sub, score in kwargs.items() if score == max_score]
  min_subjects = [sub.capitalize() for sub, score in kwargs.items() if score == min_score]
  average_score = sum(kwargs.values()) / len(kwargs)
  return {
          "highest" : (top_subjects, max_score),
          "lowest" : (min_subjects, min_score),
          "average" : average_score
  }
def main():
  subject_infos = {}
  user_name = input("Enter your name: ")
  print(f"\n---Welcome {user_name.title()}! Enter subject info---")
  while True:
    print("Type 'stop' to finish")
    key = input("Enter a subject: ")
    if key.lower() == 'stop':
      break
    value = get_number(f"Enter the score of {key}: ")
    subject_infos[key] = value
  if subject_infos:
    result = analyze_stats(**subject_infos)
    print("\n" + "~" * 30)
    print(f"---Subject info about {user_name.title()}---")
    print("-" * 30)
    #the highest scores
    subjects, score = result['highest']
    print(f"- The highest score is ({score}): {', '.join(subjects)}")
    #the lowest score
    subjects, score = result['lowest']
    print(f"- The lowest score is ({score}): {', '.join(subjects)}")
    #average score
    print(f"- Average score: {result['average']:.1f}")
    print("\n" + "~" * 30)
  else:
    print("No info entered")
if __name__ == "__main__":
  main()