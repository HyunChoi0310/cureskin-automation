from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.click_page import ClickPage
from pages.base_page import Page


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.click_page = ClickPage(self.driver)
        self.base_page = Page(self.driver)
