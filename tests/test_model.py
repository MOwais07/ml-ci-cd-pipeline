import unittest
import numpy as np
from app.main.model import predict


class TestModel(unittest.TestCase):
    def test_predict(self):
        data = np.array([1, 2, 3])
        result = predict(data)
        self.assertTrue((result == np.array([2, 4, 6])).all())


if __name__ == "__main__":
    unittest.main()
