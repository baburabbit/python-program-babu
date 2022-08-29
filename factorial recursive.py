def recursive_factorial(n):
  if (n==1):
     return n
  else:
     return n*recursive_factorial(n-1)
number = int(input("enter the number : "))
print("factorial of given number is", recursive_factorial(number))


