from fastapi import FastAPI,HTTPException,status,Path,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,EmailStr,AnyUrl,Field,ValidationError
from typing import List,Dict,Optional,Annotated
import json

Mark = Annotated[int, Field(ge=1, le=100)]
class Student(BaseModel):
    name:Annotated[str,Field(...,max_length=50,description='Name should be within 50 characters',examples=['Chandra'])]
    email:EmailStr
    marks:Annotated[List[Mark],Field(...,min_length=1,description='Atleast 1 subject marks required')]

class PutStudent(BaseModel):
    name:Optional[Annotated[str,Field(max_length=50)]]
    email:Optional[EmailStr]
    marks:Annotated[List[Mark],Field(min_length=1)]


def load_data():
    with open('students.json','r') as f:
        students = json.load(f)

    return students

def save_data(data):
    with open('students.json','w') as f:
        json.dump(data,f)

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Student Management System"}

@app.get('/about')
def about():
    return {"message ":"A fully functional API to manage your Student record"}


@app.get('/students')
def students_details():
    data = load_data()
    return data

@app.get('/student/{id}')
def get_student(id:int=Path(...,description='ID of the Student in the DB',examples='1')):
    data = load_data()
    student = next(
            (std for std in data if std['id'] == id),
            None)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    return student

@app.post('/students')
def create_student(student:Student):
    data = load_data()
    next_id = max((std['id'] for std in data), default=0) + 1

    new_student = {
        'id': next_id,
        'name': student.name,
        'email': student.email,
        'marks': student.marks
    }
    data.append(new_student)
    print(data)
    save_data(data)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=new_student)

@app.put('/students/{req_id}')
def put_student(req_id:int,putstudent:Student):
    data = load_data()
    student = next(
            (std for std in data if std['id'] == req_id),
            None)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )

    update_data = putstudent.model_dump()

    student.update(update_data)

    save_data(data)
    print(student)
    return JSONResponse(status_code=status.HTTP_200_OK,content=student)

@app.delete('/students/{req_id}')
def del_student(req_id:int):
    data = load_data()
    student = next(
            (std for std in data if std['id'] == req_id),
            None)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )

    print(student)
    data.remove(student)
    save_data(data)
    return JSONResponse(status_code=status.HTTP_200_OK,content=student)

