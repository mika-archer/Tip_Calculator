#PEMDAS
#()
#**
#*
#/ or //
#+
#-

#f-string = f"str {random_presestablished_insert}"


#Prompts in the terminal
print('Welcome to your Bill Splitter!')
bill = float(input("What is you total bill amount? $"))
tip = int(input('Gratuity percent wanting to give: 10, 12, or 15? '))
people = int(input('How many to split with? '))


#Affiliated math for the gratuity/tip
tip_as_percent = tip / 100
total_tip_amount_as_an_int = bill * tip_as_percent
total_bill_amount = bill + total_tip_amount_as_an_int
bill_per_person = total_bill_amount / people
bill_with_tip = tip / 100 * bill
round(bill_per_person, 2)

final_amount = round(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person) #to round to two decimal places

#Final solution
print(f'PAY TOTAL - ${final_amount}')
