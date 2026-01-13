# Given a sorted array and a target, return indices of two numbers whose sum equals the target.

arr = [1, 1, 2, 2, 3]
target = 5

left = 0
right = len(arr)-1

for x in range(len(arr)):
    if arr[left] + arr[right] == target:
        print(f"The no are: {arr[left]} & {arr[right]}")
        break
    
    elif arr[left] + arr[right] < target:
        left += 1
    
    elif arr[left] + arr[right] > target:
        right -= 1