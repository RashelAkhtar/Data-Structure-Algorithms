# Find the largest and smallest element in an array.

arr = [12, 13, -511, 100, -1]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(f"Largest Element: {largest}")
print(f"Smallest Element: {smallest}")