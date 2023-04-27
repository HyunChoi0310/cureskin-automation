from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(Page):

    #CLICK_HAMBURGER = (By.CSS_SELECTOR, 'summary.header__menu-item.header__active-menu-item.header__menu-item--top.list-menu__item.focus-inset')
    #CLICK_HAMBURGER = (By.CSS_SELECTOR, '.icon.icon-hamburger')
    CLICK_FACE_WASHES = (By.XPATH, '//a[@class="header__menu-item list-menu__item focus-inset"]/span[contains(text(), "Face Washes")]')
    PRICE_RANGE_LOWER = (By.CSS_SELECTOR, '.price-range__thumbs.is-lower')

    # def click_hamburger(self):
    #     self.click(*self.CLICK_HAMBURGER)
    def click_face_washes(self):
        self.click(*self.CLICK_FACE_WASHES)

    # def drag_and_drop_by_lower(self, lower):
    #     action = ActionChains(self.driver)
    #     print(f"Lower value: {lower}")
    #     element = self.driver.find_element(By.CSS_SELECTOR, '.price-range__thumbs.is-lower')
    #     source_element = element.get_attribute("aria-valuenow")
    #     print(f"Source element value: {source_element}")
    #     target_locator = (
    #     By.XPATH, f"//div[@class='price-range__thumbs is-lower']/following-sibling::div[@aria-valuenow='Rs. {lower}']")
    #     print(f"Target locator: {target_locator}")
    #     wait = WebDriverWait(self.driver, 20)
    #     target_element = wait.until(EC.presence_of_element_located(target_locator))
    #     action.drag_and_drop(element, target_element)
    #     action.perform()
    #     target_value = target_element.get_attribute("aria-valuenow")
    #     print(f"Target value: {target_value}")


    def drag_and_drop_by_lower(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '.price-range__thumbs.is-lower')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, 50, 0)
        action.perform()

    def drag_and_drop_by_upper(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '.price-range__thumbs.is-upper')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, -50, 0)
        action.perform()
