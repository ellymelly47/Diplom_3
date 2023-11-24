import allure
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполняем почту в инпуте "Email"')
    def fill_email(self, email):
        self.send_keys_to_element(BasePageLocators.INPUT_EMAIL, email)

    @allure.step('Заполняем пароль в инпуте "Пароль"')
    def fill_password(self, password):
        self.send_keys_to_element(BasePageLocators.INPUT_PASSWORD, password)

    @allure.step('Выполняем логин кликом на кнопку "Войти"')
    def click_on_enter_button(self):
        self.click_on_element(3, LoginPageLocators.ENTER_BUTTON)

    @allure.step('Переходим на страницу восстановления пароля кликом на ссылку "Восстановить пароль"')
    def click_on_password_recovery_link(self):
        self.click_on_element(3, LoginPageLocators.RESET_PASSWORD_LINK)
