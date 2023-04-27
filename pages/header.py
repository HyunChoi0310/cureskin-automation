from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    CLICK_SHOP_PRODUCT = (By.XPATH, '//summary[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop by Product")]')
    CLICK_ALL_PRODUCT = (By.XPATH, '//a[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span[contains(text(), "Shop All")]')

    def click_shop_product(self):
        self.click(*self.CLICK_SHOP_PRODUCT)

    def click_all_product(self):
        self.click(*self.CLICK_ALL_PRODUCT)