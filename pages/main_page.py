import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Переходим на страницу логина кликом по кнопке "Войти в аккаунт"')
    def click_on_enter_account_button(self):
        self.move_to_element_and_click(MainPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Раскрываем всплывающее окно с деталями ингредиента кликом на ингредиент')
    def click_on_ingredient(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Закрываем всплывающее окно с деталями ингредиента кликом на крестик')
    def click_on_close_button(self):
        self.move_to_element_and_click(BasePageLocators.CLOSE_BUTTON)

    @allure.step('Подтверждаем создание заказа кликом на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавляем ингредиент "Флюоресцентная булка" в корзину заказа')
    def move_bun_to_basket(self):
        self.move_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Говяжий метеорит (отбивная)" в корзину заказа')
    def move_filling_to_basket(self):
        self.move_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Соус Spicy-X" в корзину заказа')
    def move_sauce_to_basket(self):
        self.move_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получаем количество добавленного в корзину ингредиента')
    def get_counter_number_of_ingredient_bun(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создаем заказ и получаем его номер')
    def make_order(self):
        self.wait_until_element_visibility(10, MainPageLocators.INGREDIENT_BUN)
        self.move_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.move_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_the_element(10, MainPageLocators.ORDER_BUTTON)
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)
        self.wait_until_element_visibility(10, MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_until_element_invisibility(10, MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(BasePageLocators.CLOSE_BUTTON)
        return order
