# VeroSkills

Note:

```py
my_dict = {'name': "Tyler", 'age': 39}

print('Tyler' in my_dict.values())
print('name' in my_dict.keys())

my_string = "the quick brown fox jumped over the lazy dog"

char_dict = {}

for char in my_string:
    if char in char_dict.keys():
        char_dict[char] += 1
    else:
        char_dict[char] = 1
    
print(char_dict)
```

