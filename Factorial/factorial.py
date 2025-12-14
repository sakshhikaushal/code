"""
factorial code

input = 4
output = 24

input
loop = 1*2 -> 2*3 -> 6*4
mul = 1 * 1
mul = 1 * 2
mul = 2 * 3
mul = 6 * 4

mul 1*2*3*4
mul - define
print = output
"""

mul = 1
num = int(input("enter number: "))
for fac in range(1, num +1):
    mul = fac * mul
print(mul)