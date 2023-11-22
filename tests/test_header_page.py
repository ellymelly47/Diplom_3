import allure
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestHeaderPage:

    @allure.title('Проверка редиректа по клику на кнопку "Лента заказов" в хедере')
    def test_redirect_by_order_list_button(self, driver):

        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        assert feed_page.find_the_element(5, FeedPageLocators.ORDERS_LIST_TITLE).is_displayed(), \
            'Не удалось перейти на страницу с заказами по клику на кнопку "Лента заказов"'

    @allure.title('Проверка редиректа по клику на кнопку "Конструктор" в хедере')
    def test_redirect_by_constructor_button(self, driver):

        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)
        feed_page.wait_until_element_visibility(5, FeedPageLocators.ORDERS_LIST_TITLE)
        header_page.click_on_constructor()
        main_page = MainPage(driver)

        assert main_page.find_the_element(5, MainPageLocators.CONSTRUCTOR_TITLE).is_displayed(), \
            'Не удалось перейти на главную страницу по клику на кнопку "Конструктор"'

    @allure.title('Проверка редиректа по клику на кнопку "Личный кабинет" в хедере')
    def test_redirect_by_account_button(self, driver, login):

        main_page = MainPage(driver)
        main_page.find_the_element(10, MainPageLocators.INGREDIENT_BUN)
        header_page = HeaderPage(driver)
        header_page.click_on_account()
        profile_page = ProfilePage(driver)

        assert profile_page.find_the_element(5, ProfilePageLocators.PROFILE_LINK).is_displayed(), \
            'Не удалось перейти на страницу профиля по клику на кнопку "Личный кабинет"'
