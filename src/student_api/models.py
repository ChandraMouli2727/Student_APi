from pydantic import BaseModel,EmailStr,Field
from typing import List,Annotated

Mark = Annotated[int, Field(ge=1, le=100)]
class Student(BaseModel):
    name:Annotated[str,Field(...,max_length=50,description='Name should be within 50 characters',examples=['Chandra'])]
    email:EmailStr
    marks:Annotated[List[Mark],Field(...,min_length=1,description='Atleast 1 subject marks required')]

class Response_Student(BaseModel):
    id:int
    name:str 
    email:EmailStr
    marks:List[Mark]