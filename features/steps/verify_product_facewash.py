from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.click_page import ClickPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@given('Open CureSkin Product main page')
def open_cureskin_shop(context):
    context.app.main_page.open_main()


@when('Click hamburger menu')
def click_hamburger_menu(context):
    context.app.click_page.click_hamburger()


@when('Click shop by product')
def click_shop_by_product(context):
    context.app.click_page.click_shop_product()

@when('Click face washes')
def click_face_washes_list(context):
    context.app.click_page.click_face_washes()

@then('Verify the products showed')
def verify_show_face_washes(context):
    context.app.verify_face_washes_count()