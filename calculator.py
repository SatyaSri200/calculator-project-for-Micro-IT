# simple calculator
num1=float(input("enter the first number: "))
operator=input("enter the operator: ")
num2=float(input("enter the second number: ")) 
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)   
elif  operator=="*":
    print(num1*num2)
elif operator=="/":
    if(num2!=0):
        print(num1/num2)
    else:
        print("division is not possible")
else:
    print("invalid operator")        
