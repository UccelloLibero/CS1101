import math


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y


def test_sqrt():
    for a in range(1, 26):
        my_squareroot = my_sqrt(a)
        math_squareroot = math.sqrt(a)
        print("a =", a, " | ", "my_sqrt(a) =",my_squareroot, " | ", "math.sqrt(a) =", math_squareroot, " | ", "diff =", abs(my_squareroot - math_squareroot))

# function call
test_sqrt()
