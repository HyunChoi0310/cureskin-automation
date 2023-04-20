from selenium.webdriver.common.by import By
from pages.base_page import Page

class ClickPage(Page):

    CLICK_HAMBURGER = (By.CSS_SELECTOR, 'summary.header__menu-item.header__active-menu-item.header__menu-item--top.list-menu__item.focus-inset')
    #CLICK_HAMBURGER = (By.CSS_SELECTOR, '.icon.icon-hamburger')
    CLICK_SHOP_PRODUCT = (By.CSS_SELECTOR, '.menu-drawer__menu-item.list-menu__item.animate-arrow.focus-inset.menu-drawer__menu-item--active')
    CLICK_FACE_WASHES = (By.CSS_SELECTOR, 'a.menu-drawer__menu-item.list-menu__item.focus-inset.menu-drawer__menu-item--active')

    def click_hamburger(self):
        self.click(*self.CLICK_HAMBURGER)

    def click_shop_product(self):
        self.click(*self.CLICK_SHOP_PRODUCT)

    def click_face_washes(self):
        self.click(*self.CLICK_FACE_WASHES)

