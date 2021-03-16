# Create a function that takes a list of numbers  as a parameter and
# Returns the count of how many numbers in the list are divisible by 5

# globally available list of numbers I know are definitely divisible by 5 to test that the function works
numbers_list = [5, 10, 15, 20]

def divisible_by_five(numbers):
  # I have to have a variable that will hold the count for how many numbers in the list are divisible by 5, I will declare a variable named count and initialize it with a value 0
  count = 0
  # for each number in the list called numbers check if when number divided by 5 has any remainder
  for number in numbers:
    if number % 5 == 0: # precondition
      # if no remainder increase the count by one
      count += 1
  # return updated value of how many numbers are divisible by 5
  return count

#test that function still works with global list of value that I know are divisible by 5
print(divisible_by_five(numbers_list))


# passing a list of numbers as an argument
print(divisible_by_five([25, 32, 19, 101]))

print(divisible_by_five([17, 5, 100, 241, 15]))
