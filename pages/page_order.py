from pages.page_base import PageScooterBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Url
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class PageScooterOrder(PageScooterBase):

    label_scooter          = [By.XPATH, ".//div[text()='Для кого самокат']"]
    label_about_rent       = [By.XPATH, ".//div[text()='Про аренду']"]
    label_order_confirmed  = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    label_station          = [By.XPATH, ".//div[text()='{}']"]
    label_duration         = [By.XPATH, ".//div[text()='{}']"]

    input_name             = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_last_name        = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_address          = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_station          = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    input_number           = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    input_date             = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    input_comment          = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    button_next            = [By.XPATH, ".//button[text()='Далее']"]
    button_order           = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    button_yes             = [By.XPATH, ".//button[text()='Да']"]
    
    dropdown_duration      = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]
    
    checkbox_black         = [By.XPATH, ".//label[@for='black']"]
    checkbox_gray          = [By.XPATH, ".//label[@for='grey']"]

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
    
    def set_first_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    def set_last_name(self, name):
        self.driver.find_element(*self.input_last_name).send_keys(name)

    def set_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    def set_station(self, station):
        self.driver.find_element(*self.input_station).click()
        self.driver.find_element(self.label_station[0], self.label_station[1].format(station)).click()

    def set_number(self, number):
        self.driver.find_element(*self.input_number).send_keys(number)

    def set_date(self, date):
        element = self.driver.find_element(*self.input_date)
        element.send_keys(date)
        element.send_keys(Keys.RETURN)  # Прячем, чтобы не мешать выбрать срок аренды

    def set_duration(self, duration):
        self.driver.find_element(*self.dropdown_duration).click()
        self.driver.find_element(self.label_duration[0], self.label_duration[1].format(duration)).click()

    def set_black_scooter(self, is_black):
        if is_black:
            self.driver.find_element(*self.checkbox_black).click()

    def set_gray_scooter(self, is_gray):
        if is_gray: 
            self.driver.find_element(*self.checkbox_gray).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)
                                
    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()
        self.wait_for_visibility_of(self.label_rent())

    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()
        self.wait_for_visibility_of(self.button_confirm())
        
    def click_button_confirm(self):
        self.button_confirm().click()
        self.wait_for_visibility_of(self.label_confirmed())

    # @allure.step('Заполняем поля личных данных заказчика')
    def fill_your_info(self, first_name, last_name, address, station, number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_station(station)
        self.set_number(number)
        self.click_button_next()

    # @allure.step('Заполняем поля деталей заказа')
    def fill_rent_info(self, date, duration, is_black, is_gray, comment):
        self.set_date(date)
        self.set_duration(duration)
        self.set_black_scooter(is_black)
        self.set_gray_scooter(is_gray)
        self.set_comment(comment)
        self.click_button_order()         
            