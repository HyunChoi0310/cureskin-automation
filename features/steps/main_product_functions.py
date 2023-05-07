from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.base_page import Page
from pages.header import Header
from pages.verify_page import VerifyPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@given('Open CureSkin Product main page')
def open_cureskin_shop(context):
    context.app.main_page.open_main()


@when('close the popup window')
def close_popup(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, '.popup-close').click()


@when('Click hamburger menu')
def click_hamburger_menu(context):
    context.app.search_page.click_hamburger()


@when('Click shop by product')
def click_shop_by_product(context):
    context.app.header.click_shop_product()


@when('Click face washes')
def click_face_washes_list(context):
    context.app.search_page.click_face_washes()


@then('The search results page URL contains {query}')
def verify_show_face_washes(context, query):
    context.app.base_page.verify_url_contains_query(context.driver, query)


@when('Click on Shop All section')
def click_shop_all(context):
    context.app.header.click_all_product()


@when('Adjust the Price lower')
def adjust_price_filter_lower(context):
    context.app.search_page.drag_and_drop_by_lower()


@when('Adjust the Price upper')
def adjust_price_filter_higher(context):
    context.app.search_page.drag_and_drop_by_upper()


@then('Verify that number of products changes')
def verify_product_number_change(context):
    expected_text = '18 products' #all products counts
    context.app.verify_page.verify_number_not_same(expected_text)


@then('Verify that products displayed within the Price filter')
def verify_within_price(context):
    context.app.verify_page.verify_all_products_are_in_the_fiter_range()
