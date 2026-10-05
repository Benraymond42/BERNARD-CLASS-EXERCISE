students = {
    "Bernard": {"age": 20, "location": "Nairobi"},
    "Raymond": {"age": 21, "location": "Mombasa"},
    "Steven": {"age": 19, "location": "Kajiado"},
    "Mark": {"age": 22, "location": "Nakuru"}
}

print(students)



students = {
    "Bernard": {"age": 20, "location": "Nairobi"},
    "Raymond": {"age": 21, "location": "Mombasa"},
    "Steven": {"age": 19, "location": "Kisumu"},
    "Mark": {"age": 22, "location": "Nakuru"}
}

# ADD a student
students["John"] = {"age": 23, "location": "Eldoret"}

# EDIT a student
students["Bernard"]["age"] = 21

# DELETE a student
del students["Mark"]

print(students)
