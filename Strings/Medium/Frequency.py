# Count frequency of each character.

c = "Hello, how are you"
d = {}

count = 1

for x in c:
    d[x] = d.get(x, 0) + 1

print(d)

# ------------------------------------------------------------------------------------

ch = "Hello, World!"
h = {}

for x in ch:
    if x in h:
        h[x] += 1
    else:
        h[x] = 1

print(h)