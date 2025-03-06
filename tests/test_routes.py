import unittest
from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict(self):
        response = self.app.post("/predict", json={"input": [1, 2, 3]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["prediction"], [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
