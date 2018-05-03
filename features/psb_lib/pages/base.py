from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(locator))
        WebDriverWait(self.driver, 20).until(ec.visibility_of(element))
        element.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def switch_to_desired_window(self, desired_url, current_windows_count):
        WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(current_windows_count+1))
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if self.driver.current_url == desired_url:
                break

    def get_element_text(self, element):
        element = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(element))
        return element.text

    def element_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(locator))
        return element.is_displayed()
