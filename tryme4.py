# predefined function provided to us
# function that prints a new line - - with a dot for readability
def new_line():
  print('.')

# predefined function provided to us
# function that prints three lines where new_line() function we defined before is initialized within the three_lines() function
# function printing 3 new lines
def three_lines():
  new_line()
  new_line()
  new_line()

# function that utilizes the concept of nested functions - a function initialized within another function
# function printing 9 lines
def nine_lines():
  three_lines()
  three_lines()
  three_lines()

# function initialized with multiple functions that were previously declared
# printing total of 25 new lines
def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

# calling function that prints 9 new lines, with dot for each line for visual presentation
nine_lines()

# print statement as a placeholder between new lines for visual presentation
print("Nine lines were printed!")

# print statement placeholder explaining that we will print 25 more new lines
print("Next we'll print 25 new lines!")

# calling function that prints 25 new lines, dots for each line for visual presentation
clear_screen()


# References

# FreeCodeCamp. (2020, January 5). Nested Functions in Python. https://www.freecodecamp.org/news/nested-functions-in-python/

# Downey, A. (2015). Chapter 3: Functions. In Green Tea Press (Ed.). Think Python: How to think like a computer scientist.This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) https://greenteapress.com/thinkpython2/html/thinkpython2004.html
