from pages.page_base import PageScooterBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Url


class PageScooterHome(PageScooterBase):

    buttons_order = [By.XPATH, ".//button[text()='Заказать']"]
    button_status = [By.XPATH, ".//button[text()='Статус заказа']"]

    def __init__(self, driver):
        super().__init__(driver, Url.home)
        self.driver = driver

    # Локаторы часто задаваемых вопросов:
    # Не вынесено в переменные, чтобы избежать повторений, так как все локаторы имеют одинаковый формат.
    def faq_heading(self, number):
        return self.driver.find_element(By.XPATH, ".//div[@id='accordion__heading-" + str(number) + "']") 

    def faq_panel(self, number):
        return self.driver.find_element(By.XPATH, ".//div[@id='accordion__panel-" + str(number) + "']") 

    def click_faq_section(self, number):
        # element.click() не работает, так как мешает сообщение о куках.
        # Можно конечно и принять куки, но проще с помощью JS кликнуть по кнопке напрямую:
        # https://stackoverflow.com/questions/49252880/element-is-not-clickable-at-point-x-y-5-because-another-element-obscures-it
        self.driver.execute_script("arguments[0].click();", self.faq_heading(number))

    def wait_for_panel(self, number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(self.faq_panel(number)))

    def faq_section_visible(self, number):
        return self.faq_panel(number).is_displayed()

    def click_button_order_top(self):
        self.driver.find_elements(*self.buttons_order)[0].click()

    def click_button_order_bottom(self):
        button_order = self.driver.find_elements(*self.buttons_order)[1]
        self.driver.execute_script("arguments[0].click();", button_order)

    def button_status_displayed(self):
        return self.driver.find_element(*self.button_status).is_displayed()
        