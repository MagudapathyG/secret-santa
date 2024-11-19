import unittest
from santa.secret_santa import SecretSanta
from santa.employee import Employee

class TestSecretSanta(unittest.TestCase):
    def test_assignments(self):
        employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com")
        ]
        previous_assignments = {}

        secret_santa = SecretSanta(employees, previous_assignments)
        assignments = secret_santa.assign()

        self.assertEqual(len(assignments), len(employees))
        self.assertTrue(all(giver != recipient for giver, recipient in assignments))
