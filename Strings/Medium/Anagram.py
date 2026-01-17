# Check if two strings are anagrams.

c1 = "Cat"
c2 = "Act"
c1 = c1.lower()
c2 = c2.lower()
d1 = {}
d2 = {}

if len(c1) != len(c2):
    print(f"{c1} & {c2} are not anagrams!")
    exit()

for x in c1:
    d1[x] = d1.get(x, 0) + 1

for x in c2:
    d2[x] = d2.get(x, 0) + 1

print(d1)
print(d2)

if d1 == d2:
    print(f"{c1} & {c2} are anagrams!")
else:
    print(f"{c1} & {c2} are not anagrams!")

