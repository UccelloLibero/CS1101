# PART 1
aristotle = 'Educating the mind without educating the heart is no education at all.'
words = aristotle.split()
print(words)
print("\n")

pop_word = words.pop(0) # removing first word of the list and assigning it to a new variable
print(pop_word)
print("\n")

words.remove("no") # the word “no” will be removed from the list of words
print(words)

del words[3] # word at index 3 will be removed - "without"
print(words)

words.sort() # sort() by ascending by default.
print(words)

words.append("said by Aristotle") # adds word to the end of the word
print(words)

words.extend(["Once upon a time"]) # adds the specified list elements (or any iterable) to the end of the current list.
print(words)

words.insert(0, "Supporting evidence shows") # inserts the specified value at the specified position.
print(words)

separator = " "
updated_list = separator.join(words)
print(updated_list)


# PART 2
# nesting
travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print("Travel Expenses")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number, sum(week)))
    week_number += 1

# "*" operator
mood = ["happy"]
updated_mood = mood * 10
print(updated_mood)

# list slicing
pack_for_trip = ['passport', 'wallet', 'laptop', 'towel', 'backpack', 'tent', 'umbrella']

first_two_items = pack_for_trip[0:2]
print(first_two_items) # first and second item

third_and_forth_item = pack_for_trip[2:4]
print(third_and_forth_item) # third and fourth item

last_two_items = pack_for_trip[5:]
print(last_two_items) # last two items

# the "+=" operator
song_part1 = ['if', 'you', 'are', 'happy']
song_part2 = ['and', 'you', 'know', 'it']
song_part3 = ['clap', 'your', 'hands']
all_together_now = song_part1 + song_part2 + song_part3
print(all_together_now)


# filtering
# function will create a new empty list and add every element from the list that has an odd index. The function should then return this new list.

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    if index % 2 != 0:
      new_lst.append(lst[index])
  return new_lst


print(odd_indices([5, 4, 7, 22, 11, -3])) # output should be [4, 22, -3] because these numbers are at the indices 1, 3 and 5

# legal but unexpected operation
list_of_words = ['sunshine', 'moon', 'stars', 'lake', 'trees']
insert_new_word = list_of_words.extend('mountains')
print(list_of_words)
correct_extention = list_of_words.extend(['mountains'])
print(list_of_words)
