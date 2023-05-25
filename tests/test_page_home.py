import pytest
import allure
from pages.page_order import PageScooterOrder
from pages.page_home import PageScooterHome
from urls import Url 
import data


@allure.feature('Тестируем домашнюю страницу')
class TestPageScooterHome:

    @allure.title('Проверка секций часто задаваемых вопросов')
    @pytest.mark.parametrize("faq_section", data.test_data_faq, 
        ids=["Price", "Multiple", "Time", "Today", "Change", "Charger", "Cancel", "Suburbs"])
    def test_faq(self, driver, faq_section):
        page_home = PageScooterHome(driver)
        page_home.open()
        page_home.click_faq_section(faq_section)
        assert page_home.faq_section_visible(faq_section), "Не открылась секция {} часто задаваемых вопросов ".format(faq_section)

    @allure.title('Проверка перехода к странице заказа через верхнюю кнопку')
    def test_order_button_top(self, driver):
        page_home = PageScooterHome(driver)
        page_home.open()
        page_home.click_button_order_top()
        page_order = PageScooterOrder(driver)
        assert page_order.label_scooter_displayed(), "Не открылась страница заказа"

    @allure.title('Проверка перехода к странице заказа через нижнюю кнопку')
    def test_order_button_bottom(self, driver):
        page_home = PageScooterHome(driver)
        page_home.open()
        page_home.click_button_order_bottom()
        page_order = PageScooterOrder(driver)
        assert page_order.label_scooter_displayed(), "Не открылась страница заказа"

    @allure.title("Проверка перехода на страницу Яндекс")
    def test_yandex_button(self, driver):
        page_home = PageScooterHome(driver)
        page_home.open()
        page_home.click_button_yandex()
        assert page_home.title() == 'Дзен', "Не открылась страница Яндекс"
