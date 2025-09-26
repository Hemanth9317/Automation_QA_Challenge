# tests/pages/student_form_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class StudentFormPage(BasePage):
    # Locators
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    CHILD_CHECKBOX = (By.NAME, "is_child")
    PARENT_EMAIL = (By.NAME, "parent_email")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Save']")

    # Actions
    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def enter_phone(self, phone):
        self.type(self.PHONE, phone)

    def select_child(self):
        self.click(self.CHILD_CHECKBOX)

    def enter_parent_email(self, parent_email):
        self.type(self.PARENT_EMAIL, parent_email)

    def submit_form(self):
        self.click(self.SUBMIT_BTN)
