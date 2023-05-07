from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from support.logger import logger, MyListener


def browser_init(context, scenario_name):
    """
     :param context: Behave context
     :param test_name: scenario_name
     """

    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #context.driver = webdriver.Chrome(options=chrome_options)
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

#chrome
    # context.driver = webdriver.Chrome()
    # service = Service("./chromedriver.exe")
    # options = Options()
    # context.driver = webdriver.Chrome(service=service, options=options)

#EventFiringWebDriver -- log file
#for drivers
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )

#firefox
    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='.\geckodriver.exe', options=options)
    # options = webdriver.ChromeOptions()
    # #####################

# #headless--chrome
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920,1080")
#     context.driver = webdriver.Chrome(options=chrome_options)

# # headless--firefox
#     options = Options()
#     options.headless = True
#     options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")
#     context.driver = webdriver.Firefox(options=options)

# # for browerstack ###
#     # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#     bs_user = 'hyunredcloud_TPBt2u'
#     bs_key = '7jxNseRwHAsznZxPXda4'
#
#     desired_cap = {
#         'browserName': 'Firefox',
#         'bstack:options': {
#             'os': 'OS X',
#             'osVersion': 'Big Sur',
#             'sessionName': scenario_name
#         }
#     }
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
####
#Allure command
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/cureskin_product_page.feature
##
#allure serve test_results/
#####
    # mobile_emulation = {"deviceName":"Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)

def before_step(context, step):
    #print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        #print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
