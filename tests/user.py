from fastapi.testclient import TestClient
from main import app
from models.users import User

from .utils.user_gen import RandomGen

client = TestClient(app)

gen = RandomGen()


class TestUser:

    def create_user(self):

        user = User(
            display_name = gen.string_gen(8),
            password = gen.password_gen(),
            email = gen.email_gen(),
        )

        packet = {
            "display_name": user.display_name,
            "password": user.password,
            "email": user.email,
        }

        res = client.post("/users", json=packet)
        
        return res

    def test_get_user(self):
        res = client.get("/users")