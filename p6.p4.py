password=input("Enter your password:")

correct_password, incorrect_password = 0,0

print("Please enter password three times)
while correct_password <3 and incorrect_password !="":
    
    if password == "password1":
     correct_password +=1
     print ("Correct Password Entered")
     password = input("Enter your password:")
     if correct_password ==2:
       print ("You have successfully logged in")
       exit()
     
    else:
     incorrect_password +=1
     print ("Incorrect Password, Please try again.")
     password = input("Enter your password:")
     if incorrect_password ==2:
         print("Incorrect password entered too many times. You have been denied access.")
         exit()
     
   
   
     

    

