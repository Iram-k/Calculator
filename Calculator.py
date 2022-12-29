class maths:
    def Addition(num1,num2):
        add = num1 + num2
        print('Sum of ',num1 ,'and' ,num2 ,'is :',add)
    def Subtraction (num1,num2):
        subtract = num1 - num2
        print('Difference of ',num1 ,'and' ,num2 ,'is :',dwhile)
    def Multiplication(num1,num2):
        mul = num1 * num2
        print('Product of' ,num1 ,'and' ,num2 ,'is :',mul)
    def Division(num1,num2):
        div = num1 / num2
        print('Division of ',num1 ,'and' ,num2 ,'is :',div)
    def Floor_Division(num1,num2):
        floor_div = num1 // num2
        print('Floor Division of ',num1 ,'and' ,num2 ,'is :',floor_div)
    def power(num1,num2):
        power = num1 ** num2
        print('Exponent of ',num1 ,'and' ,num2 ,'is :',power)
    def Modulus(num1,num2):
        modulus = num1 % num2
        print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)


print("MATHEMATICAL CALCULATIONS")
cd=True
while cd:
    print(" 1. Addition ")
    print(" 2. Subtraction ")
    print(" 3. Multiplication ")
    print(" 4. Division ")
    print(" 5. Floor Division")
    print(" 6. power")
    print(" 7. Modulus")
    print(" 8. Exit")
    choice=int(input("Enter your choice (1-8): "))

    if choice==1:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Addition(a,b)
    elif choice==2:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Subtraction(a,b)
    elif choice==3:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Multiplication(a,b)
    elif choice==4:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Division(a,b) 
    elif choice==5:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Floor_Division(a,b)
    elif choice==6:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.power(a,b)
    elif choice==7:
        a = int(input('Enter First number: '))
        b = int(input('Enter Second number '))
        maths.Modulus(a,b)
    elif choice==8:
        print("Do you want to exit? Yes/No")
        option=input( )
        if option=='yes' or option=='Yes' or option=='y' or option=='Y':
            break                        
        else:
            var=True
            
