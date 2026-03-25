def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      #for factorial it's better to use int instead of float
      return int(input(prompt))
    except ValueError:
      print("Please enter only numbers, Try again")
def find_factorial(number):
  """a function that finds the factorial"""
  #checking negative numbers
  if number < 0:
    return "The factorial of a negative number does not exist"
  #checking the number if its equal to zero
  elif number == 0:
    return 1
  #calculate for all remaining positive numbers
  else:
    factorial = 1
    #for loop is inside the function
    for i in range(1, number + 1):
      factorial = factorial * i
    return factorial
      
      #-----MAIN PART-----
#asking a number from the user
num = get_number("Enter a number")
#we run the function and save the answer to the 'result'
result = find_factorial(num)
#we will screen the answer
print(f"Factorial of {num}: {result}")