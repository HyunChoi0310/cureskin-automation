from pages.base_page import Page
from support.logger import logger

class MainPage(Page):
    def open_main(self):
        self.open_url('https://shop.cureskin.com/')
        logger.info('Opening url https://shop.cureskin.com/')