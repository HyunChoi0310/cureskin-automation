from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class VerifyPage(Page):
    NUMBER_CHANGE = (By.ID, 'ProductCount')
    FILTER_PRICE = (By.CSS_SELECTOR, '.facets__price > div')
    ITEMS_LIST = (By.CSS_SELECTOR, '.price-item.price-item--sale')


    def verify_number_not_same(self, expected_text):
        sleep(2)
        self.verify_text_contains_not_same(expected_text, *self.NUMBER_CHANGE)


    def verify_all_products_are_in_the_fiter_range(self):
        filtered_price = self.find_element(*self.FILTER_PRICE).text
        #print("filtered:", filtered_price)
        first_price = float(filtered_price.replace('Price: Rs. ', '').replace(' — Rs. 546', '').replace(',', '').split(' ')[0])
        #print("first:", first_price)
        second_price = float(filtered_price.replace('Price: Rs. 180 — Rs. ', '').replace(',', '').replace('— Rs. ', ''))
        #print("second:", second_price)

        elements = self.find_elements(*self.ITEMS_LIST)

        item_price_list = []

        # iterate over the elements and extract the price value
        for element in elements:
            price_text = element.text.strip()  # get the text content of the element
            price_value = float(price_text.replace('Rs.', '').replace(',', '').strip()) # manipulate the string to extract the price value
            #print("price_value:", price_value)  # print the extracted price value
            if price_value >= first_price and price_value <= second_price:
                item_price_list.append(price_value)
            else:
                print("The price in out of the filter range", price_text)
        #print(item_price_list)