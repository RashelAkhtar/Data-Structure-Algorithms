# Find the first non-repeating character.

c = "Hello, World!"
d = {}

for x in c:
    d[x] = d.get(x, 0) + 1

for x in d:
    if d[x] == 1:
        print(x)
        break
