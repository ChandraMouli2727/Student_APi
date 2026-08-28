from fastapi import FastAPI,HTTPException,status,Path,APIRouter
from fastapi.responses import JSONResponse
from student_api.database import save_data,load_data
from student_api.models import Student,Response_Student
from typing import List

router = APIRouter()
@router.get("/")
def home():
    return {"message":"Student Management System"}

@router.get('/about')
def about():
    return {"message ":"A fully functional API to manage your Student record"}


@router.get('/students',response_model=List[Response_Student])
def students_details():
    data = load_data()
    return data

@router.get('/student/{id}',response_model=Response_Student)
def get_student(id:int=Path(...,description='ID of the Student in the DB',examples='1')):
    data = load_data()
    student = next(
            (std for std in data if std['id'] == id),
            None)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    return student

@router.post('/students',response_model=Response_Student)
def create_student(student:Student):
    data = load_data()
    next_id = max((std['id'] for std in data), default=0) + 1

    new_student = {
        'id': next_id,
        'name': student.name,
        'email': student.email,
        'marks': student.marks
    }
    data.routerend(new_student)
    print(data)
    save_data(data)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=new_student)

@router.put('/students/{req_id}',response_model=Response_Student)
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

@router.delete('/students/{req_id}')
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
