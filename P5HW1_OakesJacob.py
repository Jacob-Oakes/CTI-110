#Jacob Oakes
#10/11/23
#Uing functions


#Create function

def adding(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

#Main func
def main():
    user_choice = 0

    while user_choice != 3:
        
        print("welcome to the Main menu")
        print("-------------------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. End program")

        user_choice = int(input("Enter one through three: "))        

        if user_choice == 1:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a number: "))
            print(adding(num1, num2))
        if user_choice == 2:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a number: "))
            print(subtract(num1, num2)) 
        if user_choice == 3:
            print("Goodbye")
            


        else:
            print("You entered an invaild choice")

#Calling main
main()
