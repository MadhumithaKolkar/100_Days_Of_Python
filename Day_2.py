print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10,12, or 15? "))
share = (tot_bill+((percentage_tip/100)*tot_bill))/num_people
print("Each person should pay: $",share)