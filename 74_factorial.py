#---- THIS IS THE OLD VERSION OF MY CODE---
#def get_number(prompt):
  #"""a function that only accepts integers from the user"""
  #while True:
    #try:
      #for factorial it's better to use int instead of float
      #return int(input(prompt))
    #except ValueError:
      #print("Please enter only numbers, Try again")
#def find_factorial(number):
  #"""a function that finds the factorial"""
  #checking negative numbers
  #if number < 0:
    #return "The factorial of a negative number does not exist"
  #checking the number if its equal to zero
  #elif number == 0:
    #return 1
  #calculate for all remaining positive numbers
  #else:
    #factorial = 1
    #for loop is inside the function
    #for i in range(1, number + 1):
      #factorial = factorial * i
    #return factorial
      
      #-----MAIN PART-----
#asking a number from the user
#num = get_number("Enter a number")
#we run the function and save the answer to the 'result'
#result = find_factorial(num)
#we will screen the answer
#print(f"Factorial of {num}: {result}")

#---THIS IS THE NEW VERSION MUCH MORE BETTER THAN THE OLD ONE---
def get_number(prompt):
  """ a function that only accepts integers from the user"""
  while True:
    try:
      #for factorial it's better to use int instead of float
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers")
def find_factorial(num):
  """ a function that finds the factorial of given number"""
  #checking negative numbers
  if num < 0:
    return "The factorial of a negative number does not exist"
  #calculate for all remaining numbers
  factorial = 1
  for i in range(1, num + 1):
    factorial *= i
  return factorial
#---Main Part---
while True:
  #asking a number from the user
  number = get_number("Enter a number to find its factorial: ")
  #we run the ptoject and save the result to the (result) variable
  result = find_factorial(number)
  #displaying the result to the user
  print(f"The factorial of {number} is equal to {result}")
  #asking from the user if he/she wants to stop the project
  choice = input("Do do you want to check a number again? (yes/no)").lower()
  #checking if the user wants to stop
  if choice == 'no':
    print("The project was ended, GoodBye")
    break