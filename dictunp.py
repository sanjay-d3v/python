from pprint import pprint
values = {}
for x in range(5):
    values[x] = x*2
# [comprehension for item in items] #comprehension expression
# values = {x: x*2 for x in range(5)}
print(values)

sentence = "this is a common question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1

    else:
        char_frequency[char] = 1
print(char_frequency)
pprint(char_frequency, width=1)
