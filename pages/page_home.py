from pages.page_base import PageScooterBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Url


class PageScooterHome(PageScooterBase):

    heading_faq = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    heading_panel = [By.XPATH, ".//div[@id='accordion__panel-{}']"]
    buttons_order = [By.XPATH, ".//button[text()='Заказать']"]
    button_status = [By.XPATH, ".//button[text()='Статус заказа']"]

    def __init__(self, driver):
        super().__init__(driver, Url.home)
        self.driver = driver

    # Локаторы часто задаваемых вопросов:
    def faq_heading(self, number):
        return self.driver.find_element(self.heading_faq[0], self.heading_faq[1].format(number))

    def faq_panel(self, number):
        return self.driver.find_element(self.heading_panel[0], self.heading_panel[1].format(number))

    def click_faq_section(self, number):
        # element.click() не работает, так как мешает сообщение о куках.
        # Можно конечно и принять куки, но проще с помощью JS кликнуть по кнопке напрямую:
        # https://stackoverflow.com/questions/49252880/element-is-not-clickable-at-point-x-y-5-because-another-element-obscures-it
        self.execute_script_on("arguments[0].click();", self.faq_heading(number))
        self.wait_for_visibility_of(self.faq_panel(number))

    def faq_section_visible(self, number):
        return self.faq_panel(number).is_displayed()

    def click_button_order_top(self):
        self.driver.find_elements(*self.buttons_order)[0].click()
        self.wait_for_url(Url.order)

    def click_button_order_bottom(self):
        button_order = self.driver.find_elements(*self.buttons_order)[1]
        self.execute_script_on("arguments[0].click();", button_order)
        self.wait_for_url(Url.order)

    def button_status_displayed(self):
        return self.driver.find_element(*self.button_status).is_displayed()
        