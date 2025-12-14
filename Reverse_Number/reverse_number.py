"""
num = int(input("Enter +ve Number: "))
new_num = 0

print("num-->",num)

# num = 094788

while num != 0:
    rem = num % 10
    num = num // 10
    new_num = new_num * 10 + rem
"""
"""
input = 674556
output = 654567
"""
"""
Only last 2 digits revered in ones, rest revered in tens
rem = 674556 % 10 = 6
num (quo) = 674556 // 10 = 67455
new_num = 0(new_num pre defined) * 10 + 6(rem) = 6

rem = 6745 % 100 = 45
num(quo) = 6745 //100 = 67
new_num = new_num in above while loop * 100 + rem
"""

num = int(input("enter +ve positive: "))
new_num = 0
count = 0

while num != 0 and count < 2:
    rem = num % 10
    num = num // 10
    new_num = new_num * 10 + rem
    count = count + 1
    
while num != 0:
    rem = num % 100
    num = num // 100
    new_num = new_num * 100 + rem
    
print(new_num)    
