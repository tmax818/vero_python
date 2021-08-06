# VeroSkills

Note:

``` python

times = range(1, 101)

for item in times:
     print("Hello, World") 
    
def squares(number):
    """prints the square of a sequence up to the number supplied"""
    numbers = range(1, number+1)
    for i in numbers:
        print(i * i)
        
Challenge

def squares_list(number):
    squares = []
    numbers = range(1, number + 1)
    for i in numbers:
        squares.append(i * i)
    return squares
    
print(squares_list(6))
```