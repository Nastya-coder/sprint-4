from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import *


class PageScooterBase:

    # Локаторы
    button_yandex = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    button_scooter = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

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

    def click_button_yandex(self):
        self.driver.find_element(*self.button_yandex).click()
        self.switch_tab(1)  # Открывается в новой вкладке

    def click_button_scooter(self):
        self.driver.find_element(*self.button_scooter).click()
        self.wait_for_url(Url.home)
    