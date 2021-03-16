#importing math module to calculate the square root of the a**2 + b**2
import math

# Hypotenuse is the longest side of a right-angled triangle, the side that is opposite the right angle
# Pythagorean theorem formula: a**2 + b**2 = c**2

# define a function to calculate the longest side of the right triangle knowing the length of the other two sides:

def hypotenuse(a, b):
  csquared = a**2 + b**2
  right_side = math.sqrt(csquared)
  return right_side

# testing the complete version of hypotenuse function
print(hypotenuse(3, 4))
print(hypotenuse(5, 12))
print(hypotenuse(6, 8))
