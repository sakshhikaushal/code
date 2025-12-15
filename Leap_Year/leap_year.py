"""
User will give input, year is leap year or not.
is leap year then print leap, else - not leap year
"""

# centuries = that has to be divisible by 100 as well as 400 - then only it will be leap year
# non-century - should only be divisible by 4


year = int(input("enter number = "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
elif year % 4 == 0:
    print ("Leap year")
else:
    print("Not Leap Year")

