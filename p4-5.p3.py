gross_income = int(input('enter a euro value:'))
if gross_income >0:
    print ('Gross income:', gross_income)
else:
    print ('Amount of income must be >0. Please try again.')

lower_tax_amount = gross_income / 10 * 6

higher_tax_amount = gross_income / 10 * 4

lower_tax = lower_tax_amount / 100 *13.5

higher_tax = higher_tax_amount / 100 * 23

total_tax = lower_tax + higher_tax

net_income = gross_income - total_tax

if net_income >0:
    print ('Net income:',net_income)


print ('Finished')
