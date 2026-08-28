from fastapi import HTTPException,status,Path,APIRouter,Depends,Header,Request
from fastapi.responses import JSONResponse
from student_api.database import load_data
from student_api.models import Student,Response_Student
from typing import List
from student_api.services import create_student,get_all_students,get_student_by_id,update_student,del_student


router = APIRouter()
def get_students_data()->List[dict]:
   return load_data()

def get_current_user(User:str=Header(alias="User"))->str:
    if User.upper() != 'CHANDRA':
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User')
    return User

protected_router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/")
def home():
    return {"message":"Student Management System"}

@router.get('/about')
def about():
    return {"message ":"A fully functional API to manage your Student record"}


@router.get('/students',response_model=List[Response_Student])
def students_details(data:list[dict]=Depends(get_students_data)):
    return get_all_students(data)

@router.get('/student/{s_id}',response_model=Response_Student)
def get_student(s_id:int=Path(...,description='ID of the Student in the DB',examples='1'),data=Depends(get_students_data)):
    response = get_student_by_id(data,s_id)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    return response


@protected_router.post('/students',response_model=Response_Student)
# def create_student(student:Student,data:List[dict]=Depends(get_students_data),user=Depends(get_current_user)):
def post_student(student:Student,data:List[dict]=Depends(get_students_data)):
    response = create_student(student,data)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=response)

@protected_router.put('/students/{req_id}',response_model=Response_Student)
def put_student(req_id:int,putstudent:Student,data:List[dict] = Depends(get_students_data)):
    response = update_student(req_id,data,putstudent)
    if response is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    
    return JSONResponse(status_code=status.HTTP_200_OK,content=response)

@protected_router.delete('/students/{req_id}')
def delete_student(req_id:int,data:List[dict] =Depends(get_students_data)):
    response = del_student(req_id,data)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Student Id not found' )
    return JSONResponse(status_code=status.HTTP_200_OK,content=response)
