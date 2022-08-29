number1=int(input("enter the number1:"))
number2=int(input("enter the number2:"))
number3=int(input("enter the number3:"))
if(number1>number2) and (number1>number3):
    greater=number1
elif(number2>number1) and (number2>number3):
    greater=number2
else:
    greater=number3
print("greater of three number is:",greater)
