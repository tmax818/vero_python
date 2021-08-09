---
title: Intro to Python
...

# VERO_PYTHON


1. [introduction](./lessons/01lesson/index.html)

   ## Lesson Objective

   - Provide a brief introduction to the course, the Python programming language and practice with the VeroSkills interface.

   - Python Origins
     - [Guido van Rossum](https://gvanrossum.github.io)
     - Monty Python
   - Why Python?
     - reads like English

### Python's Hello, World

```python
print("Hello, World")
```

### C's Hello, World

```c
#include <stdio.h>

int main(void)
{
puts("Hello, World");
return 0;
}
```
   - `help(<python keyword>)` to access documents



2. [data types](./lessons/02lesson/index.html) 
   - 


3. [programming logic](./lessons/03lesson/index.html)


4. [variables and strings](./lessons/04lesson/index.html)


5. [flow control](./lessons/05lesson/index.html)


6. [fizzbuzz](./lessons/06lesson/index.html)



7. [while loop](./lessons/07lesson/index.html)



8. [functions_part1](./lessons/08lesson/index.html)

   - step up in difficulty
   - docstrings
   - return value


9.  [functions_part2](./lessons/09lesson/index.html)

   - parameters/arguments
   - scope

10. [sequences](./lessons/10lesson/index.html)



11. [lists](./lessons/11lesson/index.html)


12. [tuples](./lessons/12lesson/index.html)



13. [ranges and `for`](./lessons/13lesson/index.html)



14. [dictionaries](./lessons/14lesson/index.html)


15. [classes](./lessons/15lesson/index.html)


16. [Python Standard Library](./lessons/16lesson/index.html)

   - Introduction to the Python Standard Library
   - Batteries Included
   - VERY large library of modules for various programming related tasks

```python
import webbrowser

webbrowser.open("https://docs.python.org/3/library/")
```

```python

import urllib.request, json

with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
    data = json.loads(url.read().decode())
    print(data['bpi']['USD']['rate'])
```