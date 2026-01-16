# Squares of a sorted array with O(n)

# Two Pointer Approch
arr = [-4, -1, 0, 1, 3, 10]

left = 0
right = len(arr) - 1

while left < right:
    if abs(arr[left]) < abs(arr[right]):
        arr[right] = arr[right] * arr[right]
        right -= 1
    else:
        arr[left] = arr[left] * arr[left]
        arr[right], arr[left] = arr[left], arr[right]
        right -= 1

print(arr)