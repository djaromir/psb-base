from selenium import webdriver
from features.psblib.pages.base import *


def before_all(context):
    context.driver = webdriver.Firefox()
    context.driver.set_page_load_timeout(10)
    context.driver.maximize_window()
    context.base_page = BasePage(context.driver)


def after_all(context):
    context.driver.quit()
