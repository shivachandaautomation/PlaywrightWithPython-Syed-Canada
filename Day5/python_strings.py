# Python strings: definition, slicing, and common methods

# Creating a string
name = "Alice"
print("Name:", name)

# String indexing and slicing
print("First character:", name[0])
print("Last character:", name[-1])
print("Characters 1 to 4:", name[1:4])
print("Every second character:", name[::2])
print("Reversed string:", name[::-1])

# String length
print("Length:", len(name))

# Changing case
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title case:", name.title())

# Searching and checking
text = "Python is easy and fun"
print("Contains 'easy'?:", "easy" in text)
print("Index of 'easy':", text.index("easy"))
print("Count of 'a':", text.count("a"))
print("Starts with 'Python'?:", text.startswith("Python"))
print("Ends with 'fun'?:", text.endswith("fun"))

# Stripping spaces and splitting
message = "   Hello, World!   "
print("Trimmed:", message.strip())
print("Split by space:", message.split())
print("Split by comma:", "apple,banana,grape".split(","))

# Joining strings
words = ["Python", "is", "awesome"]
print("Joined string:", " ".join(words))

# Replacing text
sentence = "I like Java"
print("After replace:", sentence.replace("Java", "Python"))

# String formatting
age = 25
print("My age is {}".format(age))
print(f"My age is {age}")

# Checking type and emptiness
print("Is it alphabetic?", "Alice".isalpha())
print("Is it numeric?", "123".isdigit())
print("Is it alphanumeric?", "Alice123".isalnum())
print("Is empty?", "".isspace())

# Find substring positions
sample = "learning python programming"
print("Find 'python':", sample.find("python"))
print("Find 'Java':", sample.find("Java"))

# Escape sequences
print("New line example:\nHello")
print("Tab example:\tHello")
print("Quote example: \"Hello\"")

# String concatenation
first = "Hello"
last = "World"
print("Concatenated:", first + " " + last)
