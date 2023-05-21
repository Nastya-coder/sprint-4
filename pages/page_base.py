from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageScooterBase:

    # Локаторы
    button_yandex = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    button_scooter = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(self.url))

    def click_button_yandex(self):
        self.driver.find_element(*self.button_yandex).click()

    def click_button_scooter(self):
        self.driver.find_element(*self.button_scooter).click()
