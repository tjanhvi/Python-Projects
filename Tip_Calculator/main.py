#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")

bill = float(input("Total bill: "))
people = int(input("Total people: "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))

tip_percent = tip/100
total_tip_amount = tip_percent*bill
total_bill = bill + total_tip_amount
each_person = total_bill/people
final_amount = round(each_person,2)
print(f"Each person will pay {final_amount}")

