# Find the second largest element in an array.

arr = [11, 21, 13, 4, 58]

largest = arr[0]
sec_largest = arr[0]

for i in arr:
    if i > largest:
        largest = i
        
for i in arr:    
    if i > sec_largest and i != largest:
        sec_largest = i

print(f"Largest: {largest}")
print(f"Second Largest: {sec_largest}")


# ----------------------------------------------------------------------------------------- #
# Another Solution with better Time Complixity #

arr2 = [23, 21, 56, 91, 45]

lrg = float('-inf')   # -inf = -ve infinite & inf = +ve infinite
sec_lrg = float('-inf')

for x in arr2:
    if x > lrg:
        sec_lrg = lrg
        lrg = x
    
    elif x > sec_lrg and x != lrg:
        x = sec_largest

print(f"Largest: {lrg}")
print(f"Second Largest: {sec_lrg}")      