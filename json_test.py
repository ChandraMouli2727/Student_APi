import json
with open("students.json","r") as f:
    students = json.load(f)

print(students)
for std in students:
    print(std['name'])

