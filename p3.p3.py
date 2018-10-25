gross_income = 143523
print ('Gross income:', gross_income)

lower_tax_amount = gross_income / 10 * 6

higher_tax_amount = gross_income / 10 * 4

lower_tax = lower_tax_amount / 100 *13.5

higher_tax = higher_tax_amount / 100 * 23

total_tax = lower_tax + higher_tax

net_income = gross_income - total_tax

print ('Net income:',net_income)
