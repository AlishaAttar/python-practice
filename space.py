text = "Python is a powerful programming language"

result = ""

for char in text:
    if char != " ":
        result += char

print("Original:", text)
print("Without spaces:", result)