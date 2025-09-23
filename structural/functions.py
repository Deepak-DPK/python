# ============================================
# 1. New Line: \n
# ============================================
# The \n character forces the text to break to a new line.

print("--- 1. New Line (`\\n`) ---")
print("Hello\nWorld!")
# Output:
# Hello
# World!
print("\n") # Adds a blank line for spacing


# ============================================
# 2. Tab: \t
# ============================================
# The \t character inserts a horizontal tab space.

print("--- 2. Tab (`\\t`) ---")
print("Column A\tColumn B")
print("Value 1\t\tValue 2")
# Output:
# Column A        Column B
# Value 1         Value 2
print("\n")


# ============================================
# 3. Double Quotes: \"
# ============================================
# Use \" to put a double quote inside a string that is also defined by double quotes.

print('--- 3. Including Quotes (`\\"`) ---')
# Method 1: Using an escape sequence
print("He said, \"Python is amazing!\"")

# Method 2: Using single quotes to define the string
print('He said, "Python is amazing!"')
# Both methods produce the same output:
# He said, "Python is amazing!"
print("\n")


# ============================================
# 4. Backslash: \\
# ============================================
# Since a single backslash starts an escape sequence, use \\ to print one literal backslash.

print('--- 4. Literal Backslash (`\\\\`) ---')
# This is common for Windows file paths.
print("File located at: C:\\Users\\Deepak")
# Output:
# File located at: C:\Users\Deepak
print("\n")