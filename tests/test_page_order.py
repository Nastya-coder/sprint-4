import pytest
# import allure

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.page_home import PageScooterHome
from pages.page_order import PageScooterOrder

from urls import Url 
import data


class TestPageScooterOrder:

    driver = None

    # @allure.step('Открываем браузер Firefox')
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()

    # @allure.step('Заполняем поля личных данных заказчика')
    def fill_your_info(self, page_order, first_name, last_name, address, station, number):
        page_order.set_first_name(first_name)
        page_order.set_last_name(last_name)
        page_order.set_address(address)
        page_order.set_station(station)
        page_order.set_number(number)
        page_order.click_button_next()

    # @allure.step('Заполняем поля деталей заказа')
    def fill_rent_info(self, page_order, date, duration, is_black, is_gray, comment):
        page_order.set_date(date)
        page_order.set_duration(duration)
        page_order.set_black_scooter(is_black)
        page_order.set_gray_scooter(is_gray)
        page_order.set_comment(comment)
        page_order.click_button_order()      

    # @allure.title('Проверка страницы личных данных заказчика')
    @pytest.mark.parametrize("first_name, last_name, address, station, number", 
        data.test_data_your_info, ids=["Nastya", "Nina"])
    def test_your_info(self, first_name, last_name, address, station, number):
        page_order = PageScooterOrder(self.driver)
        page_order.open()
        self.fill_your_info(page_order, first_name, last_name, address, station, number)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.label_rent()))
        assert page_order.label_rent_displayed()

    # @allure.title('Проверка страницы деталей заказа')
    @pytest.mark.parametrize("date, duration, is_black, is_gray, comment", 
        data.test_data_rent_info, ids=["Black", "Gray"])
    def test_rent_info(self, date, duration, is_black, is_gray, comment):
        page_order = PageScooterOrder(self.driver)
        page_order.open()
        self.fill_your_info(page_order, *data.test_data_your_info[0])
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.label_rent()))
        self.fill_rent_info(page_order, date, duration, is_black, is_gray, comment)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.button_confirm()))
        assert page_order.button_confirm_displayed()

    # @allure.title('Проверка страницы подтверждения заказа')
    @pytest.mark.parametrize("user_info, rent_info", data.test_data_confirmation, ids=["Nastya", "Nina"])
    def test_order_confirmation(self, user_info, rent_info):
        page_order = PageScooterOrder(self.driver)
        page_order.open()
        self.fill_your_info(page_order, *user_info)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.label_rent()))
        self.fill_rent_info(page_order, *rent_info)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.button_confirm()))
        page_order.click_button_confirm()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(page_order.label_confirmed()))
        assert page_order.label_confirmed_displayed()

    # @allure.title("Проверка перехода на домашнюю страницу")
    def test_scooter_button(self):
        page_home = PageScooterHome(self.driver)
        page_home.open()
        page_home.click_button_scooter()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.home))
        assert self.driver.current_url == Url.home and page_home.button_status_displayed()  
    
    # @allure.step('Закрываем браузер')
    @classmethod
    def teardown_class(self):
        self.driver.quit()
