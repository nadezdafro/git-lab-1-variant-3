import unittest
from app import completion_percent, remaining_tasks


class TestProject(unittest.TestCase):
    def test_half(self):
        self.assertEqual(completion_percent(2, 4), 50)

    def test_all(self):
        self.assertEqual(completion_percent(5, 5), 100)

    def test_invalid_total(self):
        with self.assertRaises(ValueError):
            completion_percent(1, 0)

    def test_remaining(self):
        self.assertEqual(remaining_tasks(2, 5), 3)

    def test_remaining_all(self):
        self.assertEqual(remaining_tasks(5, 5), 0)


if __name__ == "__main__":
    unittest.main()
