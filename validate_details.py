import re

def validate_first_name(first_name):
    if len(first_name) < 2:
        raise ValueError("First name must be at least 2 characters long.")
    return True

def validate_last_name(last_name):
    if len(last_name) < 2:
        raise ValueError("Last name must be at least 2 characters long.")
    return True

def validate_mobile_number(mobile):
    pattern = re.compile(r'^[0-9]{10}$')
    if not pattern.match(mobile):
        raise ValueError("Mobile number must be a 10-digit number.")
    return True

def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not pattern.match(email):
        raise ValueError("Email must be in a valid format.")
    return True

def validate_pin_code(pin_code):
    if len(pin_code) != 6 or not pin_code.isdigit():
        raise ValueError("Pin code must be a 6-digit number.")
    return True

