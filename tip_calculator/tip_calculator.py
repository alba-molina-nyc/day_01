"""pre_tip_total = input('what was the total bill: ')
tip_percentage = input('what is the percentage you`d like to leave on this bill: ')
num_people = input('how many people will you be splitting this bill with: ')
percent = int(tip_percentage) / 100 
tip_calculation = percent * int(pre_tip_total)
post_tip_total = int(tip_calculation) + int(pre_tip_total)
even_split = int(post_tip_total) / int(num_people) 
converted_split = int(even_split)

print(f'each person pays {converted_split}, you your POST TIP TOTAL is {post_tip_total}, you would like to SPLIT this bill among {num_people} you would like to leave a {tip_percentage} PERCENT on a bill TOTAL of: {pre_tip_total}')"""


# TODO figure out how to use typescript to send it to an html file

#collect data from people
bill = float(input('what was the total bill: '))
tip = int(input('what is the percentage you`d like to leave on this bill: '))
people = int(input('how many people will you be splitting this bill with: '))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person)
print(f'each person should pay {final_amount}')