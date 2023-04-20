from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
        logger.info(f'Inputting text: {text}')

    def verify_text(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    def verify_text_contains(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert actual_result[:30:] == expected_text[:30:], f'Expected {expected_text} but got {actual_result}'

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