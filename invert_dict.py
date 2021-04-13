# four highest peaks in Colorado
dictionary = {'Mount Elbert': '2', 'Mount Massive': '2', 'Mount Harvard': '1', 'Blanca Peak': '3'}



def invert_dict(d):
    inverse = dict()
    for key in d:
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
