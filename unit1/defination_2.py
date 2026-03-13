Num1=float(input("Enter The first Number"))
Num2=float(input("Enter The Second Number"))
operator=input("Operator Like +,-,*,/ you can enter on it.")

if operator == '+':
    result=Num1+Num2
    print("result is ",result)

elif operator == '-':
    result=Num1-Num2
    print("Rusult is",result)

elif operator == '*':
    result=Num1*Num2
    print("Result is :",result)

elif operator == '/':
    if Num2 == 0:
        result=Num1/Num2
        print("Result is :",result)
    else:
        print("Error:Divition By zero:")

else:
    print("Invalid Operator")