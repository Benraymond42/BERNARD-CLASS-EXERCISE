students = [
    {"name": "Bernard", "age": 20, "location": "Nairobi"},
    {"name": "Raymond", "age": 21, "location": "Mombasa"},
    {"name": "Steven", "age": 19, "location": "Eldoret"},
    {"name": "Mark", "age": 22, "location": "Nakuru"}
]

print(students)


for student in students:
    print(student["name"], "will be", student["age"] + 2, "years old in two  years.")
