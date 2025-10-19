# Dictionary example
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

# Dictionary with mixed data types
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "boolean": True,
    "nested_dict": {"key": "value"}
}

# Empty dictionary
empty_dict = {}

# Dictionary using dict() constructor
constructed_dict = dict(a=1, b=2, c=3)


print(my_dict.get("age"))
print(my_dict.keys())
print(my_dict.values())


# Accessing dictionary elements and iteration
for key,value in my_dict.items():
    print(key, ":", value)

# update 
my_dict.update({"car_model" : "bmw"})
print(my_dict)

# just return only that index value 
print(mixed_dict["list"][1])


# iterate the list 
for location in mixed_dict["list"]:
    print(location)
