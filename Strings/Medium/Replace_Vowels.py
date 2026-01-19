# Replace all vowels with *.

c = "Mori, jm moi"
vowels = {"a", "e", "i", "o", "u"}
c = c.lower()

for x in vowels:
    c = c.replace(x, "*")

print(c)