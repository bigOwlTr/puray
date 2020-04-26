import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    # def test_dot_product(self):
    #     self.assertEqual(self.v1.dot_product(), -27)

    def test_multiply(self):
        product = self.v1 * 2
        self.assertEqual(getattr(product, "x"), 2.0)

    def test_addition(self):
        sum = self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 4.0)

    def test_subtraction(self):
        sum = self.v1 - self.v2
        self.assertEqual(getattr(sum, "x"), -2.0)

    def test_divide(self):
        product = self.v1 / 2
        self.assertEqual(getattr(product, "x"), 0.5)


if __name__ == "__main__":
    unittest.main()
