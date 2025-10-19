list_of_dictionaries = {
    "person1": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    },
    "person3": {
        "name": "Bob",
        "age": 35,
        "city": "Chicago"
    }
}

for person, details in list_of_dictionaries.items():
    print(person)
    print(details["name"],"-->",details["city"])
