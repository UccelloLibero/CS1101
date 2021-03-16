# First exercise, Part 1
# function that expects a negative arg and counts up from that to zero, zero check done at first
def countup(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n+1)


# First exercise, Part 2
# program that evaluate input and calls appropriate function based on the input to count down to zero for positive numbers and up to zero for negative numbers

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def countup(n):
 	if n == 0:
   		print("Blastoff!")
 	else:
   		print(n)
   		countup(n+1)

n = int(input("How many seconds until the blastoff? "))

if n > 0:
 	countdown(n)
elif n < 0:
    countup(n)
else:
    print("Blastoff!")
