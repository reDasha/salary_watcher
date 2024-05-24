from datetime import date

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    current_salary: float
    salary_increase_date: date


class UserCreate(schemas.BaseUserCreate):
    username: str
    current_salary: float
    salary_increase_date: date
