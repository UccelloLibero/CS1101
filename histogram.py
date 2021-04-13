alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d

# Part 1:
def has_duplicates(string):
  new_histo = histogram(string)
  for key, value in new_histo.items():
    if value > 1:
      return True
  return False

for string in test_dups:
  if has_duplicates(string):
    print(string, ' has duplicates')
  else:
    print(string, ' has no duplicates')


# Part 2:
def missing_letters(string):
  new_histo = histogram(string)
  new_list = []
  for char in alphabet:
    if char not in new_histo:
      new_list.append(char)
  return ''.join(new_list)

for string in test_miss:
  new_list = missing_letters(string)
  if len(new_list):
    print(string, ' is missing letters ', new_list)
  else:
    print(string, ' uses all the letters')
