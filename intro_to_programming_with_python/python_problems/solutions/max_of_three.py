import random


var1 = random.randrange(0, 100)
var2 = random.randrange(0, 100)
var3 = random.randrange(0, 100)

# Print the input
print(var1)
print(var2)
print(var3)

# Make a temp variable to hold larger of the first two
temp = var1

# Make a temp varialbe to hold the max
var_max = -1

# Compare the first two variables
if var1 < var2:
    temp = var2
else:
    temp = var1

# Compare with third variable
if temp < var3:
    var_max = var3
else:
    var_max = temp

# Print max and check it is actually max
print("max is " + str(var_max))
print(var_max >= var1 and var_max >= var2 and var_max >= var3)
