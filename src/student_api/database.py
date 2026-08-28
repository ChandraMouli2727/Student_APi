import json

def load_data():
    with open('students.json','r') as f:
        students = json.load(f)

    return students

def save_data(data):
    with open('students.json','w') as f:
        json.dump(data,f)