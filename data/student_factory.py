# data/student_factory.py
import random
import string

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_student_data(adult=True):
    first_name = generate_random_string()
    last_name = generate_random_string()
    email = f"{first_name.lower()}.{last_name.lower()}@test.com"
    phone = f"+1{random.randint(1000000000, 9999999999)}"
    parent_email = None
    if not adult:
        parent_email = f"parent.{first_name.lower()}@test.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "adult": adult,
        "parent_email": parent_email
    }
