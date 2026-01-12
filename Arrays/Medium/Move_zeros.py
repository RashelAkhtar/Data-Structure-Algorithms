# Move all zeros to the end of the array.

arr = [1, 0, 2, 3, 0, 7]
temp = []
count_zero = 0

for i in arr:
    if i != 0:
        temp.append(i)
    else:
        count_zero += 1

for i in range(count_zero):
    temp.append(0)

print(temp)


# ------------------------------------------------------------------------------------------------------ #

# Sol. with better space complexity

arr2 = [1, 0, 2, 3, 0, 7, 0, 1]

pos = 0

for i in range(len(arr2)):
    if arr2[i] != 0:
        arr2[pos], arr2[i] = arr2[i], arr2[pos]

        pos += 1

print(arr2)