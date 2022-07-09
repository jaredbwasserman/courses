# Python concepts
Source: https://www.learnpython.org/

# Printing
Printing means writing text to the screen. A traditional first exercise when learning programming is to print `Hello, world!` to the screen. For Python this would look like:
```python
print("Hello, world!")
```

It is possible to print anything to the screen. For example, you can print the number 10:
```python
print(10)
```

# Comments
Comments are notes that are not actually run. Start a line with `#` to make a comment. You can put anything in a comment:
```python
# This is a comment
```

# Variables
Variables hold values. You can assign a value to a variable like this:
```python
a = 5
```

If you want to check the value of a variable, you can print it out:
```python
a = 5
print(a)
# 5
```

Why does this print "5" rather than "a"?

# Operators
An example of an operator is `+`. You can add two numbers with `+`:
```python
x = 5 + 5
print(x)
# 10
```

There are a few operators related to division:
```python
print(10 / 3)
# 3.3333333333333335

print(10 // 3)
# 3

print(10 % 3)
# 1
``` 

You can add strings together too:
```python
foo = "Hello, " + "world!"
print(foo)
# Hello, world!
```

# Lists
Lists let you hold a collection of values in a variable:
```python
mylist = [1, 2, 3]
```

You can access an element of a list with `[]`. Start from `0` (not `1`):
```python
print(mylist[0])
# 1

print(mylist[1])
# 2

print(mylist[2])
# 3

print(mylist[3])
# ERROR!
```

# Loops
Loops let you iterate over the elements of a list. For example:
```python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
```

The `prime` can be called anything. Think of it as a variable. Also, note that you must put a `:` at the end of the line.

# Conditions
Conditions are either `True` or `False`. For example:
```python
print(5 == 5)
# True

print(5 == 10)
# False
```

Note that `==` is used to check if two values are equal. The `=` operator is used for assignment.

You can use `if` to perform different actions depending on the value of a condition:
```python
x = 10
if x == 5:
    print("x is 5")

if x == 10:
    print("x is 10")
```

You can use `else` to specify what to do if the condition is false:
```python
x = 10
if x == 5:
    print("x is 5")
else:
    print("x is not 5")
```

Note that you must put a `:` at the end of the line (similar to `for` loops).