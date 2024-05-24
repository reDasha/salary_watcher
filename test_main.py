import jwt
import time
from fastapi.testclient import TestClient
from main import app
from config import SECRET

client = TestClient(app)

current_time = time.time()
token_expiration = current_time + 3600


def test_get_salary_with_valid_token():
    payload = {
        "sub": "3",
        "aud": [
            "fastapi-users:auth"
        ],
        "exp": token_expiration
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")

    salary_headers = {"Authorization": f"Bearer {token}"}
    salary_response = client.get("/salary", headers=salary_headers)

    assert salary_response.status_code == 200
    assert "Сотрудник" in salary_response.json()
    assert "Текущая зарплата" in salary_response.json()
    assert "Ближайшее повышение зарплаты" in salary_response.json()
    # assert salary_response.json() == {
    #     "Текущая зарплата": 100000.99,
    #     "Ближайшее повышение зарплаты": "2024-07-01",
    # }


def test_get_salary_without_token():
    response = client.get("/salary")

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


def test_get_salary_with_invalid_token():
    payload = {
        "sub": "3",
        "aud": [
            "fastapi-users:auth"
        ],
        "exp": 1
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")

    headers = {"X-Token": f"Bearer {token}"}
    response = client.get("/salary", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}
