print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
print("The total amount due, including the tip, is $" + str(round(total_bill, 2)))
people = int(input("How many people split the bill? "))
bill_per_person = total_bill / people
print("Each person should pay: $" + str(round(bill_per_person, 2)))
