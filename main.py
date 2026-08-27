from fastapi import FastAPI,HTTPException,status
import json

def load_data():
    with open('students.json','r') as f:
        students = json.load(f)

    return students

app = FastAPI()

@app.get('/students')
def students_details():
    data = load_data()
    return data

@app.get('/students/{id}')
def get_student(id:int):
    data = load_data()
    student = next(
            (std for std in data if std['id'] == id),
            None)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    return student