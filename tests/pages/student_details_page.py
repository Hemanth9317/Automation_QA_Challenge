# tests/pages/student_details_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class StudentDetailsPage(BasePage):
    STATUS_LABEL = (By.ID, "student_status")
    FAMILY_LINK = (By.ID, "family_link")

    def get_status(self):
        return self.get_text(self.STATUS_LABEL)

    def get_family_link(self):
        return self.get_text(self.FAMILY_LINK)
