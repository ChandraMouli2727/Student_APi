from pydantic import BaseModel,EmailStr,AnyUrl,Field,ValidationError
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):
    name : Annotated[str,Field(max_length=50,title='Name of the Student',description='Give the Student Name',example=['Chandra'])]
    email:EmailStr
    marks:List[int]

def insert_student_data(student:Student):
    print(student.name)
    print(student.email)
    print(student.marks)
    print('Record inserted')

patient_info = {"name":"chandra",
                'email':'abcegmail.com',
                'marks':[25,33]}


try:
    student1 = Student(**patient_info)
    insert_student_data(student1)

except ValidationError as e:
    print("Student data is invalid")
    print(e)