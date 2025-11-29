"""Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""
import math
num = int(input("Enter a number: "))

sr = math.sqrt(num)
nl = math.log(num)
s1 = math.sin(num)

print(f"The square root of {num} is {sr}")
print(f"The natural logarithm of {num} is {nl}")
print(f"The sine of {num} is {s1}")