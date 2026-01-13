# Rotate an array to the right by k positions.

arr = [1, 2, 3, 4, 5]
k = 1

right_last = arr[len(arr)-1]

for x in range(len(arr)-1):
    arr[x+1] = arr[x]

print(arr)

