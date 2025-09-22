import sys

# Join arguments with a space to form the full name
# e.g., ['John', 'Smith'] becomes 'John Smith'
name = " ".join(sys.argv[1:])
print(f"Full Name: {name}")

# Create the email address
# The replace() method takes two arguments: the old and the new
email = name.lower().replace(" ", ".") + "@company.com"
print(f"Generated Email: {email}") 
