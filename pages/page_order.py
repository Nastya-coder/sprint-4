from pages.page_base import PageScooterBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Url
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class PageScooterOrder(PageScooterBase):

    label_scooter = [By.XPATH, ".//div[text()='Для кого самокат']"]
    label_about_rent = [By.XPATH, ".//div[text()='Про аренду']"]
    label_order_confirmed = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    input_elements = [By.XPATH, ".//input"]
    button_next = [By.XPATH, ".//button[text()='Далее']"]
    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    button_yes = [By.XPATH, ".//button[text()='Да']"]
    dropdown_duration = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]

    def __init__(self, driver):
        super().__init__(driver, Url.order)
        self.driver = driver

    def label_rent(self):
        return self.driver.find_element(*self.label_about_rent)
    
    def label_confirmed(self):
        return self.driver.find_element(*self.label_order_confirmed)

    def button_confirm(self):
        return self.driver.find_element(*self.button_yes)

    def label_scooter_displayed(self):
        return self.driver.find_element(*self.label_scooter).is_displayed()
    
    def label_rent_displayed(self):
        return self.label_rent().is_displayed()
    
    def label_confirmed_displayed(self):
        return self.label_confirmed().is_displayed()    
    
    def button_confirm_displayed(self):
        return self.button_confirm().is_displayed()

    def input_element(self, number):
        return self.driver.find_elements(*self.input_elements)[number]
    
    def set_first_name(self, name):
        self.input_element(1).send_keys(name)

    def set_last_name(self, name):
        self.input_element(2).send_keys(name)

    def set_address(self, address):
        self.input_element(3).send_keys(address)

    def set_station(self, station):
        self.input_element(4).click()
        self.driver.find_element(By.XPATH, ".//div[text()='" + station + "']").click()

    def set_number(self, number):
        self.input_element(5).send_keys(number)

    def set_date(self, date):
        self.input_element(1).send_keys(date)
        self.input_element(1).send_keys(Keys.RETURN)  # Прячем, чтобы не мешать выбрать срок аренды

    def set_duration(self, duration):
        self.driver.find_element(*self.dropdown_duration).click()
        self.driver.find_element(By.XPATH, ".//div[text()='" + duration + "']").click()

    def set_black_scooter(self, is_black):
        if is_black:
            self.input_element(2).click()

    def set_gray_scooter(self, is_gray):
        if is_gray: 
            self.input_element(3).click()

    def set_comment(self, comment):
        self.input_element(4).send_keys(comment)
                                
    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()
        
    def click_button_confirm(self):
        self.button_confirm().click()
            