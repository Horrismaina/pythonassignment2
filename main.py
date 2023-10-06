#Mark Horris Maina SCT211-0704/2022

# question 1
import datetime

def greet():
    print("Welcome to the Age Calculator!")
    print("Enter your year of birth to calculate your age.")

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

def calculate_age_in_months(age):
    months = age * 12
    return months

def calculate_age_in_days(age):
    days = age * 365  # Approximation for simplicity
    return days

while True:
    greet()
    try:
        birth_year = int(input("Enter your year of birth (e.g., 1990): "))
        age = calculate_age(birth_year)

        if age < 0:
            print("Invalid birth year. Please enter a valid year.")
        else:
            print("Your age is {} years.".format(age))
            print("Your age is approximately {} months.".format(calculate_age_in_months(age)))
            print("Your age is approximately {} days.".format(calculate_age_in_days(age)))

    except ValueError:
        print("Invalid input. Please enter a valid year.")

    choice = input("Do you want to calculate another age? (yes/no): ")
    if choice.lower() != 'yes':
        print("Goodbye!")
        break







#question 2

def calculate_split_bill(total_bill, tip_percentage, num_people):
    tip_percentage /= 100  # Convert tip_percentage to a decimal
    tip_amount = total_bill * tip_percentage
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / num_people
    return round(amount_per_person, 2)


total_bill = float(input("Enter the total bill amount: $"))
print("Select tip percentage:")
print("1. 10%")
print("2. 12%")
print("3. 15%")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    tip_percentage = 10
elif choice == 2:
    tip_percentage = 12
elif choice == 3:
    tip_percentage = 15
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    exit()

num_people = int(input("Enter the number of people splitting the bill: "))


amount_per_person = calculate_split_bill(total_bill, tip_percentage, num_people)
print(f"Each person should pay: ${amount_per_person}")


#question 3
weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in metres:"))

squaredheight = height * height
BMI = weight/squaredheight
print ( "your bmi is " ,BMI)

if BMI < 18.5:
    print("you are underweight")
elif 18.5 <= BMI <=24.9:
    print (" you have normal weight")
else: 
    print (" you are overweight")










#question 4
year = int (input ("Enter the year:"))

if year % 4 == 0:

    print(year , "is  a leap year.")

else :

    print(year , "is not a leap year." )