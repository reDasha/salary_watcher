from fastapi import FastAPI, Depends

from auth.auth import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from auth.database import User

app = FastAPI(
    title="Salary Watcher",
    description="Справка о зарплате",
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/token",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()


@app.get("/salary", tags=["salary"])
def get_salary(user: User = Depends(current_user)):
    return {
        "Текущая зарплата": user.current_salary,
        "Ближайшее повышение зарплаты": user.salary_increase_date,
    }
