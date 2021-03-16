# daily schedule function, time of the day based on 24 hour clock

def daily_schedule(time):
 if time <= 8:
   print("Hmm, looking a bit groggy there. Have you had your coffee and breakfast yet?")
 elif time > 8 and time < 12:
   print("Stop fiddling. This is the productive hour, use it wisely.")
 elif time == 12:
   print("Finally it's time for the first break of the day. It's lunch and tea time!")
 elif time > 12 and time < 15:
   print("Not time for siesta yet, you may have another cup of coffee though.")
 elif time > 15 and time < 17:
   print("Shhhh, it's siesta time.")
 elif time == 17 or time < 19:
   print("Time to wrap it up and get ready for supper.")
 else:
   print("That's it for the day. Get some rest.")


# utilizing input() method to supply function argument
# with error -- comment next line to fix error
time = input("What time is it? ")

# uncomment to fix the runtime error
# time = int(input("What time is it? "))

# calling the function with argument supplied by user input
daily_schedule(time)


# there is a runtime error because we are supplying an argument via our input method that is of a different type than our function requires.
# input method converts the input automatically into a string and returns it
# however our function requires an argument of an int type to be supplied so the runtime error we get is TypeError
