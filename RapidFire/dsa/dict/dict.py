# Creating a Dictionary

student = {
    "name" : "deepak",
    "age"  : 22,
    "grade": "A"
}

# Accessing Values

print(student["name"])

# Add new key
student["city"] = "Chennai"

# Update existing key
student["age"] = 22

if "name" in student:
    print("Found!")