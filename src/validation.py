from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    department: str
    start_date: str
    employment_type: str
    work_setup: str

def validate_employee(data):
    return Employee(**data)
