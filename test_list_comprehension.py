string = '01234567890123456789012345678901234567890123456789'

counter = 10
temporary_list = [string[indicator:indicator + counter] for indicator in range(0, len(string), counter)]
new_string = '.'.join(temporary_list)

print(new_string)




# Adding values ​​from two lists
list_1 = [2, 5, 8, 8, 9, 3, 6, 5]
list_2 = [5, 2, 4, 7, 8]

# Method 1:
# list_3 = []
# for indicator, _ in enumerate(list_2):
#     list_3.append(list_1[indicator] + list_2[indicator])
# print(list_3)

# Method 2:
# list_3 = []
# for indicator in range(len(list_2)):
#     list_3.append(list_1[indicator] + list_2[indicator])
# print(list_3)

# Best method:
list_3 = [sum(list(pair)) for pair in zip(list_1, list_2)]
print(list_3)

# To sum from the largest list:
from itertools import zip_longest

list_3 = [sum(list(pair)) for pair in zip_longest(list_1, list_2, fillvalue=0)]
print(list_3)