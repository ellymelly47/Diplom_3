import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Раскрываем всплывающее окно с деталями заказа кликом на заказ в разделе "Лента заказов"')
    def click_on_order(self):
        self.click_on_element(3, FeedPageLocators.ORDER_LINK)

    @allure.step('Ищем заказ с нужным номером в разделе "Лента заказов"')
    def find_order_in_order_list(self, chosen_order):
        method, locator = FeedPageLocators.ORDER_NUMBER_IN_ORDER_LIST
        locator = locator.format(chosen_order)
        return self.find_the_element(10, (method, locator))

    @allure.step('Получаем общее количество заказов, выполненных за все время')
    def get_total_orders_number(self):
        return self.get_text_from_element(FeedPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Получаем общее количество заказов, выполненных за сегодня')
    def get_today_orders_number(self):
        return self.get_text_from_element(FeedPageLocators.COMPLETED_ORDERS_TODAY)

    @allure.step('Ищем заказ с нужным номером в разделе "В работе"')
    def get_order_number_in_work_list(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_NUMBER_IN_WORK)
