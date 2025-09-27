# Leap Year Checker

year = int(input("Which year do you want to check? "))

# This single line checks all the leap year rules at once:
# The year must be divisible by 4, AND not divisible by 100,
# UNLESS it is also divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a leap year")