from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import logger
class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
        e.click()
        logger.info(f'Clicking element: {e}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear
        e.send_keys(text)
        logger.info(f'Inputting text: {text}')

    def verify_text(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    def verify_text_contains(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert actual_result[:30:] == expected_text[:30:], f'Expected {expected_text} but got {actual_result}'

    def verify_text_contains_not_same(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert actual_result[:2:] != expected_text[:2:], f'Expected {expected_text[:2:]} but got {actual_result[:2:]}'

    def verify_count(self, expected_count, *locator):
        actual_count = self.driver.find_element(*locator).text
        assert expected_count == actual_count, f'Expected {expected_count} but got {actual_count}'

    def store_name(self, *locator):
        store_name = self.driver.find_element(*locator).text
        return store_name

    def store_count(self, *locator):
        store_count = self.driver.find_element(*locator).text
        store_count = int(store_count)
        return store_count

    def verify_url_contains_query(self, driver, query):
        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_contains(query))