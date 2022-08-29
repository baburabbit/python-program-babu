num=int(input("Enter a number: "))    
factorial=1
if(num<0):
    print("factorial does not exit in negative number")
elif(num==0):
    print("not a factorial number")
else:
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("factorial of given number",num,"is",factorial)
