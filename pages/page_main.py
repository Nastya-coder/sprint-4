from pages.page_base import PageScooterBase
from selenium.webdriver.common.by import By
from urls import Url


class PageScooterMain(PageScooterBase):

    # Локаторы
    button_yandex = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    button_scooter = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]
    
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.driver = driver

    def click_button_yandex(self):
        self.driver.find_element(*self.button_yandex).click()
        self.switch_tab(1)  # Открывается в новой вкладке

    def click_button_scooter(self):
        self.driver.find_element(*self.button_scooter).click()
        self.wait_for_url(Url.home)