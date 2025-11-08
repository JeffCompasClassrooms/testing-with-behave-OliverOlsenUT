from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import behave_webdriver

def before_all(context):
    options = ChromeOptions()
    
    # flags the ai wanted me to add
    options.add_argument('--no-sandbox') 
    options.add_argument('--disable-dev-shm-usage') 
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    context.behave_driver = behave_webdriver.Chrome()
    
    context.behave_driver.set_page_load_timeout(15)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()