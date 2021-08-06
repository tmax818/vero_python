# VeroSkills

Note:
#functions part 1

```python
# functions part 1

def my_function():
    """this function does nothing"""
    pass

# help(my_function)

def say_hello():
    print("hello")
    
# say_hello()

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
        
fizz_buzz(5)
```