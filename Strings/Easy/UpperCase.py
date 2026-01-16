# Convert a string to uppercase without using .upper().

s = "hello"
result = ""

for x in s:
    # Get the ASCII value of character
    ascii_value = ord(x)
    # Check if the character is lower case letter
    if 97 <= ascii_value <= 122:
        # Conter to uppercase by substracting 32
        ascii_value -= 32
    # Convert to ASCII value back to character and append
    result += chr(ascii_value)

print(result)