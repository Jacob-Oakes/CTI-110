#Jacob Oakes
#10.2.2023
#Using If statements for leap year

#Get input from user

input_year = int(input("Enter Year: "))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("the year is a leap year")
else:
    print("The year is NOT a leap year")
