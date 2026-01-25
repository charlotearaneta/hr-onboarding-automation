import uuid

def generate_employee_id():
    return f"EMP-{uuid.uuid4().hex[:8]}"

def transform_employee_data(data):
    data["employee_id"] = generate_employee_id()
    return data
