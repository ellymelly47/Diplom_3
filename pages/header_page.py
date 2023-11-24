import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Переходим в Личный кабинет при клике на кнопку "Личный кабинет" в хедере')
    def click_on_account(self):
        self.move_to_element_and_click(HeaderLocators.ACCOUNT_LINK)

    @allure.step('Переходим на главную страницу при клике на кнопку "Конструктор" в хедере')
    def click_on_constructor(self):
        self.click_on_element(3, HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step('Переходим на страницу с заказами при клике на кнопку "Лента заказов" в хедере')
    def click_on_order_list(self):
        self.move_to_element_and_click(HeaderLocators.ORDER_LIST_LINK)
