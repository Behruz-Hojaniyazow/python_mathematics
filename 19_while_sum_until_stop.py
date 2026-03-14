question = "enter the number: "

print("when you want to stop \n the project write 'stop' ")

gathered = 0

value = ' '

while True:
  value = input(question)
  
  if value == 'stop':
    break
  
  gathered += int(value)
  print(f"Current total: {gathered}")
  
print("The project was ended")