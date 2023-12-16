
print("Welcome to the tip calculator.")
bill=float(input("What is the total bill?"))
tip=int(input("what percentage tip would you like to give?"))
people=int(input("How many peeople to split the bill?"))
bill_with_tip=tip/100 *bill + bill 
bill_per_person=bill_with_tip/people
print(f"Each person should pay : {round(bill_per_person, 2)}")


