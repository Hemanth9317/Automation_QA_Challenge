# helpers/validation_helpers.py
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_valid_phone(phone):
    pattern = r'^\+\d{10,15}$'
    return re.match(pattern, phone)
