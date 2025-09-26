# tests/e2e/test_student_onboarding.py
import pytest
from selenium import webdriver
from pages.student_form_page import StudentFormPage
from pages.student_list_page import StudentListPage
from data.student_factory import generate_student_data

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_adult_student(driver):
    student_data = generate_student_data(adult=True)
    form_page = StudentFormPage(driver)
    form_page.navigate("https://your-school.mymusicstaff.com/students/add")
    form_page.enter_first_name(student_data["first_name"])
    form_page.enter_last_name(student_data["last_name"])
    form_page.enter_email(student_data["email"])
    form_page.enter_phone(student_data["phone"])
    form_page.submit_form()

    list_page = StudentListPage(driver)
    list_page.navigate("https://your-school.mymusicstaff.com/students")
    list_page.search_student(student_data["first_name"])
    students = list_page.get_student_list()
    assert any(student_data["first_name"] in s.text for s in students)
