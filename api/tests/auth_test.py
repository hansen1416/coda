import unittest

from app import app, register_module
from app.auth.models import User


class TestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

        # register_module()

    def test_login(self):

        data = {"email": "a@qq.com", "password": 123}

        response = self.client.post(data, "/auth/login")

        print(response)


if __name__ == "__main__":
    unittest.main()
