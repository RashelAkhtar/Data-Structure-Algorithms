# Move all zeros to the end of the array.

arr = [1, 0, 2, 3, 0, 7]
count_zero = 0

for i in arr:
    if i == 0:
        arr.pop(i)
        print(f"Array: {arr}")
        count_zero += 1
    
for i in range(count_zero):
    arr.append(0)

print(arr)