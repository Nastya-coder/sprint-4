import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_home import PageScooterHome
from pages.page_order import PageScooterOrder


@allure.step('Открываем домашнюю страницу')
@pytest.fixture
def page_home():
    driver = webdriver.Firefox()
    yield PageScooterHome(driver)
    driver.quit()

@allure.step('Открываем страницу заказа')
@pytest.fixture
def page_order():
    driver = webdriver.Firefox()
    yield PageScooterOrder(driver)
    driver.quit()
