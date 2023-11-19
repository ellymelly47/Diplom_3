import allure
from locators.base_page_locators import BasePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Заполняем почту в инпуте "Email"')
    def fill_email(self, email):
        self.send_keys_to_element(BasePageLocators.INPUT_EMAIL, email)

    @allure.step('Переходим на страницу сброса пароля кликом на кнопку "Восстановить"')
    def click_on_password_recovery_button(self):
        self.click_on_element(3, PasswordRecoveryPageLocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку показа/скрытия пароля в инпуте "Пароль"')
    def click_on_show_password_icon(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.SHOW_PASSWORD_ICON)
