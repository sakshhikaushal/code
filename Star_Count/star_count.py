star_count = int(input("row count number = "))
for row in range(star_count):
    for col in range(row + 1):
        print("*", end= "")
    print()
if star_count <= 0:
    print("invalid number")

    # num = int(input("enter number = "))
# for seq in range(num):
#     for _ in range(1, num + 1):
#         print(_, end = " ")
#     print()

"""
num = 6
seq = 1, 2, 3, 4, 5, 6
_   = 1, 7

"""
num = int(input("enter number = "))
for seq in range(1, num + 1):
    for _ in range(1, seq + 1):
        print(_, end = " ")
    print()