# VeroSkills

Note:

```python

global_var = "global"

def local_function():
    local_var = "local"
    # global_var = "global_var inside the function"
    print("local_var is:", local_var)
    print("global_var is:", global_var)

print("global_var is:", global_var)
# print(no_var)

local_function()

# print("local_var is:", local_var)
```