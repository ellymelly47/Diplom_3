import allure
from data import UserData
from locators.base_page_locators import BasePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:

    @allure.title('Проверка редиректа по клику на ссылку "Восстановить пароль"')
    def test_redirect_to_password_recovery_page(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        base_page = BasePage(driver)

        assert base_page.find_the_element(5, PasswordRecoveryPageLocators.RESET_BUTTON).is_displayed(), \
            'Не удалось перейти на страницу восстановления пароля по клику на ссылку "Восстановить пароль"'

    @allure.title('Проверка редиректа на страницу сброса пароля по клику на кнопку "Восстановить"')
    def test_redirect_to_password_reset_page(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.fill_email(UserData.LOGIN)
        password_recovery_page.click_on_password_recovery_button()
        base_page = BasePage(driver)

        assert base_page.find_the_element(5, PasswordRecoveryPageLocators.SAVE_BUTTON).is_displayed(), \
            'Не удалось перейти на страницу сброса пароля по клику на кнопку "Восстановить"'

    @allure.title('Проверка изменения состояния инпута "Пароль" по клику на кнопку показа/скрытия пароля')
    def test_password_input_active_state(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.fill_email(UserData.LOGIN)
        password_recovery_page.click_on_password_recovery_button()
        base_page = BasePage(driver)
        base_page.wait_until_element_visibility(10, PasswordRecoveryPageLocators.SAVE_BUTTON)
        password_recovery_page.click_on_show_password_icon()

        assert base_page.find_the_element(5, BasePageLocators.INPUT_PASSWORD_ACTIVE).is_displayed(), \
            'При клике на кнопку показа/скрытия пароля поле "Пароль" не стало активным'
