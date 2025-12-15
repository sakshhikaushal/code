"""
0 1 1 2 3 5 8 13 21 34 ...

Input - 5
Output - 5th Element 3

Input - 8
Output - 8th Element 13
"""
"""
first 2 num are defined
input
sum  (0,1,1,2....n)
print the last element
"""

old = 0
latest = 1
num = int(input("enter number: "))
for summ in range(num - 2):
    new_latest = old + latest
    old = latest
    latest = new_latest
print(latest)