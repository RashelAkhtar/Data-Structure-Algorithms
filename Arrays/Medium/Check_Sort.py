# Check whether an array is sorted or not.

arr = [2, 3, 4, 1, 5, 10]
is_sort = True
n = 0

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sort = False
        break

if is_sort:
    print("It is sorted!")
else:
    print("It is not sorted!")