#prompt the user for their name
#if the entrered name is known to the program print "that is a cool name"
#if the entered name is mickey mouse or spongebob squarepants print "I'm not sure that is your name"
#else print "you have a nice name"
#End program

name = input("enter your name:")

if name == "Darren":
    print("That is a cool name!")
elif name == "Spongebob Squarepants" or name == "Mickey Mouse":
    print("I'm not sure that is your name!")
else:
    print ("You have a nice name!")

print ("Finished!")

exit()

