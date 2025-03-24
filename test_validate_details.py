import unittest
from validate_details import validate_first_name, validate_last_name, validate_mobile_number, validate_email, validate_pin_code

class TestValidateDetails(unittest.TestCase):

    def test_first_name(self):
        self.assertTrue(validate_first_name("John"))
        with self.assertRaises(ValueError):
            validate_first_name("J")

    def test_last_name(self):
        self.assertTrue(validate_last_name("Doe"))
        with self.assertRaises(ValueError):
            validate_last_name("D")

    def test_mobile_number(self):
        self.assertTrue(validate_mobile_number("9876543210"))
        with self.assertRaises(ValueError):
            validate_mobile_number("98765")

    def test_email(self):
        self.assertTrue(validate_email("john.doe@example.com"))
        with self.assertRaises(ValueError):
            validate_email("john.doe")

    def test_pin_code(self):
        self.assertTrue(validate_pin_code("123456"))
        with self.assertRaises(ValueError):
            validate_pin_code("12345")

if __name__ == '__main__':
    unittest.main()

