# Reverse a string using slicing.

s = "Hello!"

print(s[::-1])

# [::-1] is slicing with:
#     start omitted → begins at the start
#     end omitted → goes to the end
#     step = -1 → traverses the string backward

# --------------------------------------------------------------------

rev = ""
for ch in s:
    rev = ch + rev
print(rev)