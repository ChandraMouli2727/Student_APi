import json

with open("students.json", "r") as f:
    students = json.load(f)

for std in students:
    print(std['name'])


data = {
    "id": 4,
    "name": "sachin",
    "email": "sachin@example.com",
    "marks": [100, 80, 95]
}

# Add new student to the Python list
students.append(data)

# Write the updated list back to JSON
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)


for std in students:
    print(std['name'])