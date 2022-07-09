# Loop [1, 101)
for num in range(1, 101):
    to_print = ""

    # Check for 3
    if num % 3 == 0:
        to_print = "Fizz"

    # Check for 5
    if num % 5 == 0:
        to_print += "Buzz"

    # Default
    if not to_print:
        to_print = num

    print(to_print)
