import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Выходим из аккаунта кликом по кнопке "Выход"')
    def click_on_logout_button(self):
        self.click_on_element(3, ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Переходим в раздел с историей заказов кликом по ссылке "История заказов"')
    def click_on_order_history_link(self):
        self.click_on_element(3, ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Получаем номер случайного заказа в разделе "История заказов"')
    def get_order_number(self):
        return self.get_text_from_element(ProfilePageLocators.ORDER_NUMBER_IN_ORDER_HISTORY)
