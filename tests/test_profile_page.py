import allure
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):

        main_page = MainPage(driver)
        main_page.find_the_element(10, MainPageLocators.INGREDIENT_BUN)
        header_page = HeaderPage(driver)
        header_page.click_on_account()
        profile_page = ProfilePage(driver)
        profile_page.wait_until_element_visibility(5, ProfilePageLocators.PROFILE_LINK)
        profile_page.click_on_logout_button()
        login_page = LoginPage(driver)

        assert login_page.find_the_element(5, LoginPageLocators.ENTER_BUTTON).is_displayed(), \
            'Не удалось выполнить выход из аккаунта'

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_redirect_to_order_history(self, driver, login, make_order):

        header_page = HeaderPage(driver)
        header_page.click_on_account()
        profile_page = ProfilePage(driver)
        profile_page.wait_until_element_visibility(5, ProfilePageLocators.PROFILE_LINK)
        profile_page.click_on_order_history_link()

        assert profile_page.find_the_element(5, ProfilePageLocators.ORDER_STATUS).is_displayed(), \
            'Не удалось перейти в раздел "История заказов"'
