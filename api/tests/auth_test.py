import json
import unittest

from app import app


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app

        self.app.config['TESTING'] = True

    def test_login(self):

        data = {"email": "a@qq.com", "password": 123}

        with self.app.test_client() as client:

            response = client.post(
                "/auth/login", data=data, headers={"Accept": "application/json, text/plain, */*"})

            assert response.status == "200 OK"

            body = json.loads(response.get_data(as_text=True))

            assert "access_token" in body
            assert "refresh_token" in body


if __name__ == "__main__":
    unittest.main()
