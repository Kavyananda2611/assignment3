# assignment3
Task 1:
Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.

   """ def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)"""
     
5.   Calls the function with a sample number and prints the output.

     """ print(f"The factorial of the number {n} is {factorial(n)}")"""

     Task 2:
     
"""Write a Python program that:
  Asks the user for a number as input.
 
num = int(input("Enter a number: "))

  Uses the math module to calculate the:
  
 import math
 
  Square root of the number :
      sr = math.sqrt(num)
      
o   Natural logarithm (log base e) of the number
      nl = math.log(num)
      
o   Sine of the number (in radians)
     s1   = math.sin(num)
     
6.   Displays the calculated results.

   print(f"The square root of {num} is {sr}")
print(f"The natural logarithm of {num} is {nl}")
print(f"The sine of {num} is {s1}")
"""






