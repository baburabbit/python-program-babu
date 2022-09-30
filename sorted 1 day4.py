n=int(input("enter the number:"))
list=[]
for i in range(n):
   c=input("enter the string:")
   list.append(c)
list1=sorted(list)
list2=sorted(list,reverse=True)
choice=int(input("enter the choice:"))
if(choice==1):
   print("ascending order:",list1)
else:
   print("descending order:",list2)
