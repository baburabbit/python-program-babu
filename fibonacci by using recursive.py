def fibonacci_recursion(n):
   if(n<=1):
      return n
   else:
      return(fibonacci_recursion(n-1) + fibonacci_recursion(n-2))
num_terms = 12
print("The number of terms is ")
print(num_terms)
if (num_terms<=0):
   print("enter the positive number: ")
else:
   print("fibonacci numbers are:")
   for i in range(num_terms):
      print(fibonacci_recursion(i))
