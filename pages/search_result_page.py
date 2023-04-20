from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_FACE_WASHES_COUNT = (By.CSS_SELECTOR, '#ProductCount')

    def verify_face_washes_count(self):
        expected_text = 0
        context.app.base_page.verify_text(expected_text, *self.SEARCH_FACE_WASHES_COUNT)