# # original dictionary
dictionary = {"Mount Elbert": "2", "Mount Massive": "2", "Mount Harvard": "1", "Blanca Peak": "3", "Missouri Mountain": "5", "Uncompahgre Peak": "7", "Humboldt Peak": "2"}

# read from file function
def read_dictionary_file(Filename):
  my_dictionary = {}
  with open(Filename) as f1:
    for line1 in f1:
      words = line1.split()
      key1 = words[0]
      values = words[1:]
      my_dictionary[key1] = values
  return my_dictionary

print(read_dictionary_file('dictionary.txt'))

# inverted dictionary
def invert_dict(d):
  inverse = dict()
  for key in d.keys():
    values = d[key]
    for value in values:
      if value not in inverse:
        inverse[value] = [key]
      else:
        inverse[value].append(key)
  return inverse

# printing original dictionary
print(dictionary)
# printing inverted dictionary
print(invert_dict(dictionary))


# wrinting original dictionary to new .txt file
with open('string_dictionary.txt', 'a+') as f:
  for key, value in dictionary.items():
    f.write(f'{key}:{value}\n')

# writing inverted dictionary to new .txt file
with open('invert_string_dictionary.txt', 'a+') as f:
  for key, value in invert_dict(dictionary).items():
    f.write(f'{key}:{value}\n')


# input string to demonstrate string to dictionary conversion
input_string = "Mount Elbert - 2, Mount Massive - 2, Mount Harvard - 1, Blanca Peak - 3, Missouri Mountain - 5, Uncompahgre Peak - 7, Humboldt Peak - 2"

# Converting input string to dictionary
my_mountains = dict((x.strip(), y.strip())
for x, y in (element.split('-')
for element in input_string.split(', ')))

print(my_mountains)
