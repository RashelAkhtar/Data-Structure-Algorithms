# Count how many even and odd numbers are present.

arr = [1, 2, 3, 4, 5, 6, 7, 8]

totalOdd = 0
totalEven = 0

for i in arr:
    if i%2 == 0:
        totalEven += i
    else:
        totalOdd += i

print(f"Total odd: {totalOdd}")
print(f"Total even: {totalEven}")