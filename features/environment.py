from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def browser_init(context):
    # try:
    # context.driver = webdriver.Chrome()
    # service = Service("./chromedriver.exe")
    # options = Options()
    # context.driver = webdriver.Chrome(service=service, options=options)
        # except:

#firefox
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    context.driver = webdriver.Firefox(executable_path='.\geckodriver.exe', options=options)
    options = webdriver.ChromeOptions()
    # #####################
    # options = Options()
    # context.driver = webdriver.Chrome(service=service, options=options)
    # If Chrome driver is not available, then --headless
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service("./chromedriver.exe")
    # context.driver = webdriver.Chrome(options=options, service=service)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)

    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
