def add(a,s):
    if(a==0):
        return 1
    else:
        c=0
        for i in range(s,5):
            c=c+add(a-1,i)
        return c
n=int(input("enter the no:"));
if(n<=0):
    print("enter a positive integer:");
else:
    print(add(n,0));
