from fastapi.testclient import TestClient
from main import app
from models.user import User

client = TestClient(app)


def test_create_user():
    user = User("will", "pass", "email@email.email")
    packet = {
        "display_name": user.display_name,
        "password": user.password,
        "email": user.email,
    }
    res = client.post("/users", json=packet)
    print("res: ", res)


def test_get_user():
    res = client.get("/users")
    print("res: ", res)
