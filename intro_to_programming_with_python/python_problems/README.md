# Python problems

# List Overlap
Source: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Problem statement:
```
Take two lists and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
```

## Iterating over lists
Iterate over the elements of a list like this:
```python
list1 = [1, 2, 3, 4]
for element in list1:
    print(element)

# 1
# 2
# 3
# 4
```

## Checking if an element is in a list
Use `not` to negate a condition. Use `in` to check if an element is contained in a list:
```python
list1 = [1, 2, 3, 4]
if 1 in list1:
    print("1 is in list1")

if 5 in list1:
    print("5 is in list1")

if 5 not in list1:
    print("5 is not in list1")

# 1 is in list1
# 5 is not in list1
```

## Adding an element to a list
Use `append` to add an element to a list:
```python
list1 = [1, 2]
list1.append(3)
print(list1)

# [1, 2, 3]
```

## Solution
One way to solve this problem is as follows:
1. Create an empty list of common elements.
1. Loop over the elements in the first list.
   1. If the given element is part of the second list, add it to the list of common elements.
1. Return the list of common elements.

What is this solution missing? Also, think about how to optimize this solution.

# Max Of Three
Source: https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

Problem statement:
```
Implement a function that takes as input three variables and prints the
largest of the three. Do this without using the Python "max" function.
```

## Comparing numbers
Use `<` and `>` to check for inequality:
```python
if 1 < 2:
    print("1 is less than 2")

if 2 > 1:
    print("2 is greater than 1")

# 1 is less than 2
# 2 is greater than 1
```

## Solution
It is possible to compare two variables at a time, and this can be done more than once. One solution idea is:
1. Compare the first two variables.
   1. If the first variable is larger, use it in the next comparison.
   1. Otherwise, the second variable is larger, and it should be used in the next comparison.
1. Compare the larger of the first two variables with the third variable.
   1. Return the larger variable.

Think about whether this covers all cases. Think about how to optimize this solution.

# Fizz Buzz
Source: https://www.geeksforgeeks.org/fizz-buzz-implementation/

Problem statement:
```
Write a program that loops over the numbers from 1 to 100.
For multiples of 3 print "Fizz". For multiples of 5 print "Buzz".
Otherwise, print the number.
```

## Generating a range of numbers
Use `range` to generate a list of numbers. The range is inclusive for the first number and exclusive for the second number `[start, end)`. Example:
```python
for num in range(1, 6):
    print(num)

# 1
# 2
# 3
# 4
# 5
```

## Checking for multiples
A number is a multiple of another number if the remainder is 0 after division. Python has a modulo operator `%` that returns the remainder of dividing two numbers:
```python
if 10 % 2 == 0:
    print("10 is a multiple of 2")
else:
    print("10 is not a multiple of 2")

if 10 % 3 == 0:
    print("10 is a multiple of 3")
else:
    print("10 is not a multiple of 3")

# 10 is a multiple of 2
# 10 is not a multiple of 3
```

## Solution
One way to solve this problem is to:
1. Loop over the numbers from 1 to 100.
   1. If the given number has 0 remainder when divided by 3, print "Fizz".
   1. If the given number has 0 remainder when divided by 5, print "Buzz".
   1. If neither of the above is true, just print the number.

Think about how to optimize this solution.