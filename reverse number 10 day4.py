try:
   n=input("enter the number:")
except:
   ValueError
   print("enter the proper value")
else:
   def reverse(n):
       n1=""
       for i in n:
           if(i=="ch"):
            print("invalid")
           else:
            n1=n1+i
           return n1
print("given string:",n)
print("reverse string:",reverse(n))
