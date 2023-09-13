from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    email: str
    first_name: str
    second_name: str
    age: int
    phone_number: str
    current_course: str
    joined_at: str
    last_action: str
    password: str
