# is_divisable function from 6.4 chapter
def is_divisible(x, y):
  if x % y == 0:
    return True
  else:
    return False

# is_power() function assuming both numbers passed as args are positive numbers
# a is a power of b if it is divisible by b and a/b is a power of b.
def is_power(a, b):
  # test base case: if a is one it will return true, if a is not one it will look at b but still only return True if a is one becuase there is no other positive integer that is a power of 1 excet the 1 itself, when b equals 1
  if a == 1 or b == 1:
    return a == 1
  # if a is not divisible by b then it's not power, if a is divisiable by b than it is power only if a/b is a power of b
  # demonstrating recursion
  return is_divisible(a, b) and is_power(a/b, b)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
