### Basic Logic

In Python, we work with three basic logical operators:

- not
- and
- or

### Not

Not will change a boolean value to its opposite. If we start out with a boolean expression that is true, adding the `not` operator will change the expression to false.

```python
expr = True     # begin with a true expression
print(expr)     #=> True
print(not expr) # => False
```

## `not` truth tables


|p|not p|
|---|---|
|True|False|
|False|True|

a truth table shows all the possible values a outcomes of a given operation. The `not` operator is an example of a *unary operator*. This means it only operates on a single proposition. The only possible values are `True` and `False`, so the truth table is quite simple. The following is a truth table with actual propositions for illustration: 

|p |`not` p|
|:--:|:---:|
|The sky is blue| The sky is *not* blue|
|The moon is made of green cheese|*It is not the case that* the moon is made of green cheese|

The table above consists of propositions and their negations. In Python, we are doing something analogous in code. 


### And

The following is the truth table for the `and` operator:

|p|q|p `and` q|
|---|---|:---:|
|True|True|True
|True|False|False
|False|True|False
|False|False|False

The `and` operator in Python is only true if both operands are true.

```python
print(True and True)    #=> True 
print(True and False)    #=> False 
print(False and True)    #=> False 
print(False and False)    #=> False
```

### Or

The following is the truth table for the `or` operator:


|p|q|p `or` q|
|---|---|:---:|
|True|True|True
|True|False|True
|False|True|True
|False|False|False

```python
print(True or True)    #=> True 
print(True or False)    #=> True 
print(False or True)    #=> True 
print(False or False)    #=> False
```
The `or` operator in Python is only false if both operands are false.

