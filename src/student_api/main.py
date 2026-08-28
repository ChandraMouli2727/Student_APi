from fastapi import FastAPI,status,Request
from fastapi.responses import JSONResponse
from student_api.routes import router,protected_router
import json


app = FastAPI()
@app.exception_handler(ValueError)
async def json_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "The student data file contains invalid JSON."
        }
    )

app.include_router(router)
app.include_router(protected_router)
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