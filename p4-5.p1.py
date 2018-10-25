euro = int(input('enter a euro value: '))

euro_sterling_conversion_rate = 0.89

sterling_value = euro * euro_sterling_conversion_rate
             
if sterling_value > 0: 
    print ('sterling value: ' , sterling_value)
else:
    print ('amount must be >= 0')
print ('finished')
    
    
