# tests/pages/student_list_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class StudentListPage(BasePage):
    SEARCH_BOX = (By.NAME, "search")
    STUDENT_ROWS = (By.CSS_SELECTOR, "table tbody tr")

    def search_student(self, name):
        self.type(self.SEARCH_BOX, name)

    def get_student_list(self):
        return self.driver.find_elements(*self.STUDENT_ROWS)
