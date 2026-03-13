#1_login or create a new account

#we use strings for passwords to keep the '0' at the start

login = {
        "behruz" : "050708",
        "adyl" : "241008",
        "mahmut" : "031010",
        "jawahyr" : "110508",
        "sardar" : "240808"
}
#2_get user input
user =input("enter the name: ").lower()
#3_logical check
user_code = input("enter the code: ")
if user in login:
  #If the name exists, check if the password matches
  if login[user] == user_code:
    print("Welcome to our community")
  else:
    print("incorrect password")
else:
  #If the name is not found in the dictionary at all
   print("create a new account")