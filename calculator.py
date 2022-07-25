# #Body mass calculator

height = input("Enter your height in m:  ")
weight = input("Enter your weight in kg:  ")
BMI = (round(int(weight) / float(height) ** 2))
print(f"Your body mass percentage is: {BMI}")
if BMI > 16 and 18:
    print("You are underweight") 
if BMI > 18 and 25:
    print("You weight is normal") 
if BMI > 25 and 30: 
    print("You are overweight")
if BMI > 35 and 40: 
    print("You are Obesy :( ") 

# #Your life in times calcultaor

age_as_int = input("What is your current age?")
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12 
message = f"You have {days_remaining} days,  {weeks_remaining} weeks, and {months_remaining} months left."
print(message)

#if the bill is $150, split between 5 people, with 12% tip..
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, 22 or 15? "))
people = int(input("How many people to split the bill?"))
bill_with_tip = (round(bill * (1 + tip / 100 )))
print(bill_with_tip )

#Leap year calculator 
year = int(input("Wich year do you want to check?"))
#4 100 400 

if year % 4 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Leap year")
    if year % 400 == 0:
        print("Leap year")
    input("Miltiply 4 times to know the next leap year")
else: 
    print("Not a leap year")
