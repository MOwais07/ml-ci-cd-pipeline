# tests/test_model.py

import unittest
import numpy as np
from app.main.model import predict

class TestModel(unittest.TestCase):
    def test_predict(self):
        data = np.array([1, 2, 3])
        result = predict(data)
        self.assertTrue((result == np.array([2, 4, 6])).all())

# Add two blank lines after class or function definitions
if __name__ == "__main__":
    unittest.main()

# Add a newline at the end of the file
