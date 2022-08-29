chemistry=float(input("enter the mark:"))
maths=float(input("enter the mark:"))
physics=float(input("enter the mark:"))
python=float(input("enter the mark:"))
tamil=float(input("enter the mark:"))
sum=chemistry+maths+physics+python+tamil
avg=sum/5
print("average:",avg)
if(avg>=90):
    print("garde s")
elif(avg>=75):
    print("grade a")
elif(avg>=65):
    print("grade b")
elif(avg>=50):
    print("garde c")
else:
    print("fail")
