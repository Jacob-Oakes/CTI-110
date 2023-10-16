#Jacob Oakes
#10/4/2023
#Intro to loops using range()

int_1 = int(input("Enter a num: "))
int_2 = int(input("Enter a num: "))

#First num is smaller
if int_1 <= int_2:
    #Execute for loop using rane(start,stop,increment)
    for x in range(int_1, int_2+1, 5):
        print(x)

else:
    print("The first number must be smaller.")
    
