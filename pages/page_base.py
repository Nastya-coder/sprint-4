from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import *


class PageScooterBase:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.wait_for_url(self.url)

    def title(self):
        return self.driver.title

    def switch_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])        

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def wait_for_visibility_of(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(element))

    def execute_script_on(self, script, element):
        self.driver.execute_script(script, element)
    