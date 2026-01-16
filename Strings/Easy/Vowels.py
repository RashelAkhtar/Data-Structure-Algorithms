# Count vowels in a string.

s = "Hello, I am programming in Python."
s = s.lower()

count = 0
vowels = {"a", "e", "i", "o", "u"}

for x in s:
    if x in vowels:
        count += 1

print(count)