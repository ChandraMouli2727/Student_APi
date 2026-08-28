from fastapi import FastAPI
from student_api.routes import router

app = FastAPI()

app.include_router(router)

'''
main.py
    → application

routes.py
    → endpoints

models.py
    → Pydantic models

database.py
    → JSON read/write

students.json
    → data
'''