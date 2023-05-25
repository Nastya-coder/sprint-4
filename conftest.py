import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_home import PageScooterHome
from pages.page_order import PageScooterOrder


@allure.step('Создаём драйвер Firefox')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
