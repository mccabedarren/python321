#Prompy user for a string
#iterate through string and count vowels
#loop until empty string is entered



string = input('Enter a string:')
while string != "":
    counts ={i:0 for i in 'aeiouAEIOU'}
    for char in string:
        if char in counts:
            counts[char] +=1
            print (counts)
            string = input('Enter a string')


