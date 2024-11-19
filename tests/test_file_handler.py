import unittest
from santa.file_handler import FileHandler

class TestFileHandler(unittest.TestCase):
    def test_load_employees(self):
        employees = FileHandler.load_employees(r"D:\Digit\Excel_files\Employee-List.xlsx")
        self.assertGreater(len(employees), 0)
