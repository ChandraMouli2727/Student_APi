from student_api.database import save_data,load_data
from student_api.models import Student,Response_Student
from typing import List,Dict

def create_student(student,data):
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
    return new_student


def get_all_students(data):
    return data

def get_student_by_id(data,s_id):
    student = next(
                (std for std in data if std['id'] == s_id),
                None)
    return student

def update_student(req_id,data,putstudent):
    student = next(
                (std for std in data if std['id'] == req_id),
                None)
    if student is None:
        return None
    
    update_data = putstudent.model_dump()
    student.update(update_data)
    save_data(data)
    return student

def del_student(req_id,data):
    student = next(
            (std for std in data if std['id'] == req_id),
            None)
    if not student:
       return None
    
    data.remove(student)
    save_data(data)
    return student