import random

def get_number(prompt: str) -> int:
  """function that only accepts numbers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("❌️ Error: Please enter a valid number")

def generate_question() -> tuple[int, int]:
  """Generate and return two random integers between 1 and 20"""
  return random.randint(1, 20), random.randint(1, 20)
  
def check_answer(num1: int, num2: int, user_result: int) -> None:
  """Check and display answer"""
  correct = num1 * num2
  if user_result == correct:
    print(f"✅️ Congrats, you found the correct answer!")
  else:
    print(f"❌️ Wrong: Correct answer was {correct}")
    
def main() -> None:
  num1, num2 = generate_question()
  user_result = get_number(f"{num1} × {num2} = ? ")
  check_answer(num1, num2, user_result)
    
if __name__ == '__main__':
  main()