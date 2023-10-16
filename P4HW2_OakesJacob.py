#Jacob Oakes
#10/4/2023
#Use if/else statements to determine gross pay


user = ""
count = 0
total_pay = 0
while user != "Done":
    #Get input from user
    user = input("what is your name? ")

    if user != "Done":
        count = count + 1
       

        overtime = False
        ot_hours = 0
        ot_pay = 0

        #Calculate overtime - yes/no - how much
        hours_worked = float(input("How many hours have you worked? "))
        if hours_worked >40:
            overtime = True
            ot_hours = hours_worked - 40


        #Calculate ot/regular pay
        pay_rate = float(input("What is your hourly rate? "))
        if (overtime == True):
            ot_pay = 1.5 * pay_rate * (ot_hours)
        else:
            pass

        ot_pay = 0
        reg_pay = pay_rate * (hours_worked - ot_hours)
        gross_pay = reg_pay+ot_pay
        total_pay = total_pay + gross_pay

        #Display name, pay rate, num hours worked, gross pay, ot hours, ot pay
        print(user, "With your pay rate of", pay_rate,"and", hours_worked, "Hours worked,", ot_hours, "of which were overtime", 
              "your regular time pay is",reg_pay, "and our overtime pay is", ot_pay,
              "\n Your total payout for the week is", gross_pay)

#While loop breaks
print("The total number of employees entered:", count)
print(total_pay)
