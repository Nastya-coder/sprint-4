import pytest
# import allure

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.page_home import PageScooterHome
from pages.page_order import PageScooterOrder

from urls import Url 
import data


class TestPageScooterHome:

    driver = None

    # @allure.step('Открываем браузер Firefox')
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()

    # @allure.title('Проверка секций часто задаваемых вопросов')
    @pytest.mark.parametrize("faq_section", data.test_data_faq, 
        ids=["Price", "Multiple", "Time", "Today", "Change", "Charger", "Cancel", "Suburbs"])
    def test_faq(self, faq_section):
        page_home = PageScooterHome(self.driver)
        page_home.open()
        page_home.click_faq_section(faq_section)
        page_home.wait_for_panel(faq_section)
        assert page_home.faq_section_visible(faq_section)

    # @allure.title('Проверка перехода к странице заказа через верхнюю кнопку')
    def test_order_button_top(self):
        page_home = PageScooterHome(self.driver)
        page_home.open()
        page_home.click_button_order_top()
        page_order = PageScooterOrder(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.order))
        assert self.driver.current_url == Url.order and page_order.label_scooter_displayed()

    # @allure.title('Проверка перехода к странице заказа через нижнюю кнопку')
    def test_order_button_bottom(self):
        page_home = PageScooterHome(self.driver)
        page_home.open()
        page_home.click_button_order_bottom()
        page_order = PageScooterOrder(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.order))
        assert self.driver.current_url == Url.order and page_order.label_scooter_displayed()

    # @allure.title('Проверка перехода на страницу Яндекс')
    def test_yandex_button(self):
        page_home = PageScooterHome(self.driver)
        page_home.open()
        page_home.click_button_yandex()
        self.driver.switch_to.window(self.driver.window_handles[1])  # Открывается в новой вкладке
        self.driver.title == 'Дзен'

    # @allure.step('Закрываем браузер')
    @classmethod
    def teardown_class(self):
        self.driver.quit()
