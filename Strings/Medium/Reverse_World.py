# Reverse words in a sentence.

s = "Hell no stupid"

words = []
store_char = ""

for ch in s:
    if ch != " ":
        store_char += ch

    # Avoid empty strings when multiple spaces exist
    if ch == " " and store_char:
        words.append(store_char)
        store_char = ""

if store_char:
    words.append(store_char)

words = " ".join(words[::-1])

print(words)
