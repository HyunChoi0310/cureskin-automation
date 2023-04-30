from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Header(Page):
    CLICK_SHOP_PRODUCT = (By.XPATH, '//summary[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop by Product")]')
    CLICK_ALL_PRODUCT = (By.XPATH, '//a[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop All")]')

    def click_shop_product(self):
        wait = WebDriverWait(self.driver, 20)
        overlay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-overlay")))
        wait.until(EC.invisibility_of_element_located(overlay))
        element = wait.until(EC.element_to_be_clickable(self.CLICK_SHOP_PRODUCT))
        element.click()


    def click_all_product(self):
        wait = WebDriverWait(self.driver, 20)
        overlay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-overlay")))
        wait.until(EC.invisibility_of_element_located(overlay))
        element = wait.until(EC.element_to_be_clickable(self.CLICK_ALL_PRODUCT))
        element.click()