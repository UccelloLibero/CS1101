prefixes = 'JKLMNOPQ'

suffix = 'ack'

for letter in prefixes:

    if letter == "O" or letter == "Q":

        print(letter + "u" + suffix)

    else:

        print(letter + suffix)

print("\n\n")

# String slicing can accept a third parameter in addition to two index numbers. The third parameter specifies the stride, which refers to how many characters to move forward after the first character is retrieved from the string. (Tagliaferri, 2016)

# here I am omitting start and end by giving instruction with colon to slice from the very beginning to end but my strind, third parameter, is a negative number which says to start count from the end leading to the output which reverses my string

number_string = "123456789"

print(len(number_string))

slicing3 = number_string[::-1]
print(slicing3)

print("\n")
# specifying the start index and the end index, separated by a colon, and returning a part of the string
greeting = "Hello, World!"

print(len(greeting))

slicing = greeting[7:13]
print(slicing)

print("\n")
# slicing string from the start
# by leaving out the first index, the range will start at the first character and end at the specified end index
color = "magenta"

print(len(color))

slicing2 = color[:4]
print(slicing2)
