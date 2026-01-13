# Remove duplicate elements from a sorted array.

arr = [1,1,2,2,3, 4, 5, 5, 9, 9, 11, 12, 13, 13]
slow = 0

for fast in range(len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[fast], arr[slow] = arr[slow], arr[fast]

print(arr[:slow])