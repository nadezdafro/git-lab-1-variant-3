import unittest
from app import completion_percent


class TestProject(unittest.TestCase):
    def test_half(self):
        self.assertEqual(completion_percent(2, 4), 50)

    def test_all(self):
        self.assertEqual(completion_percent(5, 5), 100)

    def test_invalid_total(self):
        with self.assertRaises(ValueError):
            completion_percent(1, 0)


if __name__ == "__main__":
    unittest.main()
