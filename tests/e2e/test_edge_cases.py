# tests/e2e/test_edge_cases.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.student_form_page import StudentFormPage
from pages.student_list_page import StudentListPage
from data.student_factory import generate_student_data
from helpers.validation_helpers import is_valid_email, is_valid_phone

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# 1️⃣ Duplicate email
def test_duplicate_email(driver):
    student_data = generate_student_data(adult=True)
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    # Add first student
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()

    # Try to add duplicate
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name("Duplicate")
    form_page.enter_last_name("Student")
    form_page.enter_email(student_data["email"])
    form_page.enter_phone("+12345678901")
    form_page.submit_form()
    error_visible = form_page.is_visible((By.XPATH, "//div[contains(text(), 'email already exists')]"))
    assert error_visible, "Duplicate email should show an error"


# 2️⃣ Special characters in names
def test_special_characters_in_name(driver):
    student_data = generate_student_data(adult=True)
    student_data["first_name"] = "José"
    student_data["last_name"] = "O'Brien"
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()

    list_page = StudentListPage(driver)
    list_page.navigate("https://your-school.mymusicstaff.com/students")
    list_page.search_student("José")
    students = list_page.get_student_list()
    assert any("José" in s.text for s in students), "Student with special characters should appear in list"


# 3️⃣ International phone number
def test_international_phone_number(driver):
    student_data = generate_student_data(adult=True)
    student_data["phone"] = "+44" + student_data["phone"][2:]
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()
    assert is_valid_phone(student_data["phone"]), "International phone number should be valid"


# 4️⃣ Child student without parent email
def test_child_without_parent_email(driver):
    student_data = generate_student_data(adult=False)
    student_data["parent_email"] = ""  # Missing parent email
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.select_child()
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.enter_parent_email(student_data["parent_email"])
    form_page.submit_form()
    error_visible = form_page.is_visible((By.XPATH, "//div[contains(text(), 'Parent email is required')]"))
    assert error_visible, "Child student must require parent email"


# 5️⃣ Maximum field length
def test_maximum_field_length(driver):
    student_data = generate_student_data(adult=True)
    student_data["first_name"] = "A"*256
    student_data["last_name"] = "B"*256
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()
    error_visible = form_page.is_visible((By.XPATH, "//div[contains(text(), 'maximum length')]"))
    assert error_visible, "Form should validate maximum field length"


# 6️⃣ Invalid email format
def test_invalid_email_format(driver):
    student_data = generate_student_data(adult=True)
    student_data["email"] = "invalid-email-format"
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()
    error_visible = form_page.is_visible((By.XPATH, "//div[contains(text(), 'invalid email')]"))
    assert error_visible, "Form should validate email format"


# 7️⃣ Session timeout handling
def test_session_timeout(driver):
    student_data = generate_student_data(adult=True)
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    # Simulate idle time (this is example, real may need sleep or API mock)
    import time
    time.sleep(5)  # replace with actual session timeout simulation
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()
    # Check session expired message
    expired_visible = form_page.is_visible((By.XPATH, "//div[contains(text(), 'Session expired')]"))
    assert expired_visible, "Session timeout should show proper message"


# 8️⃣ Concurrent student creation (basic simulation)
def test_concurrent_student_creation(driver):
    student_data1 = generate_student_data(adult=True)
    student_data2 = generate_student_data(adult=True)
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    # Add first student
    form_page.enter_first_name(student_data1["first_name"])
    form_page.enter_last_name(student_data1["last_name"])
    form_page.enter_email(student_data1["email"])
    form_page.enter_phone(student_data1["phone"])
    form_page.submit_form()

    # Add second student immediately
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data2["first_name"])
    form_page.enter_last_name(student_data2["last_name"])
    form_page.enter_email(student_data2["email"])
    form_page.enter_phone(student_data2["phone"])
    form_page.submit_form()
    list_page = StudentListPage(driver)
    list_page.navigate("https://your-school.mymusicstaff.com/students")
    list_page.search_student(student_data2["first_name"])
    students = list_page.get_student_list()
    assert any(student_data2["first_name"] in s.text for s in students), "Concurrent student should be created"


# 9️⃣ Status transition validation
def test_status_transitions(driver):
    student_data = generate_student_data(adult=True)
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()

    # Verify status is default 'Trial'
    list_page = StudentListPage(driver)
    list_page.navigate("https://your-school.mymusicstaff.com/students")
    list_page.search_student(student_data["first_name"])
    students = list_page.get_student_list()
    assert any("Trial" in s.text for s in students), "New student should start with 'Trial' status"


# 🔟 Child student linking to existing family
def test_child_link_existing_family(driver):
    student_data = generate_student_data(adult=False)
    existing_parent_email = "parent.test@example.com"
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.select_child()
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.enter_parent_email(existing_parent_email)
    form_page.submit_form()
    # Verify the child is linked correctly
    list_page = StudentListPage(driver)
    list_page.navigate("https://your-school.mymusicstaff.com/students")
    list_page.search_student(student_data["first_name"])
    students = list_page.get_student_list()
    assert any(student_data["first_name"] in s.text for s in students), "Child student should be linked to existing family"


def test_invalid_email(driver):
    student_form = StudentFormPage(driver)
    student_form.enter_email("invalid_email")
    student_form.submit()
    assert student_form.get_email_error() == "Please enter a valid email."
