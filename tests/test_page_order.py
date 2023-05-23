import pytest
import allure
import data
from pages.page_home import PageScooterHome


@allure.feature('Тестируем страницу заказа')
class TestPageScooterOrder:     

    @allure.title('Проверка страницы личных данных заказчика')
    @pytest.mark.parametrize("first_name, last_name, address, station, number", 
        data.test_data_your_info, ids=["Nastya", "Nina"])
    def test_your_info(self, page_order, first_name, last_name, address, station, number):
        page_order.open()
        page_order.fill_your_info(first_name, last_name, address, station, number)
        assert page_order.label_rent_displayed(), "Не открылась секция ввода деталей заказа"

    @allure.title('Проверка страницы деталей заказа')
    @pytest.mark.parametrize("date, duration, is_black, is_gray, comment", 
        data.test_data_rent_info, ids=["Black", "Gray"])
    def test_rent_info(self, page_order, date, duration, is_black, is_gray, comment):
        page_order.open()
        page_order.fill_your_info(*data.test_data_your_info[0])
        page_order.fill_rent_info(date, duration, is_black, is_gray, comment)
        assert page_order.button_confirm_displayed(), "Не открылась панель подтверждения заказа"

    @allure.title('Проверка страницы подтверждения заказа')
    @pytest.mark.parametrize("user_info, rent_info", data.test_data_confirmation, ids=["Nastya", "Nina"])
    def test_order_confirmation(self, page_order, user_info, rent_info):
        page_order.open()
        page_order.fill_your_info(*user_info)
        page_order.fill_rent_info(*rent_info)
        page_order.click_button_confirm()
        assert page_order.label_confirmed_displayed(), "Не открылась панель успешного создания заказа"

    @allure.title("Проверка перехода на домашнюю страницу")
    def test_scooter_button(self, page_order):
        page_order.open()
        page_order.click_button_scooter()
        page_home = PageScooterHome(page_order.driver)
        assert page_home.button_status_displayed(), "Не открылась главная страница"
    