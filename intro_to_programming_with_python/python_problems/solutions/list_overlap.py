a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Solution with duplicates
c = []
for a_elem in a:
    if a_elem in b:
        c.append(a_elem)
print(c)

# Solution without duplicates
c = []
for a_elem in a:
    if a_elem in b and not a_elem in c:
        c.append(a_elem)
print(c)

# Check with set implementation
c = set(a).intersection(set(b))
print(list(c))
