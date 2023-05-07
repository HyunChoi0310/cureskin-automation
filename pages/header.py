from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Header(Page):
    CLICK_SHOP_PRODUCT = (By.XPATH, '//*[@id="menu-drawer"]/div/div/nav/ul/li[2]/details/summary/span')
    CLICK_ALL_PRODUCT = (By.XPATH, '//*[@id="menu-drawer"]/div/div/nav/ul/li[4]/a')
    #CLICK_SHOP_PRODUCT = (By.XPATH, '//summary[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop by Product")]')
    #CLICK_ALL_PRODUCT = (By.XPATH, '//a[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop All")]')

    def click_shop_product(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.CLICK_SHOP_PRODUCT))
        element.click()
        # sleep(10)
        # self.wait_for_element_click(*self.CLICK_SHOP_PRODUCT).click()

    def click_all_product(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.CLICK_ALL_PRODUCT))
        element.click()
        #self.wait_for_element_click(*self.CLICK_ALL_PRODUCT).click()