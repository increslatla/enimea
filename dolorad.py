from collections import Counter

# Counting elements in a list
list1 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
counter1 = Counter(list1)
print(counter1)  # Counter({'x': 4, 'y': 2, 'z': 2})

# Counting elements in a string
string1 = 'hello'
counter2 = Counter(string1)
print(counter2)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
