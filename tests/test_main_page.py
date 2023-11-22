import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента')
    def test_get_ingredient_details(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_ingredient()

        assert main_page.find_the_element(5, MainPageLocators.INGREDIENT_DETAILS_TITLE).is_displayed(), \
            'При клике на ингредиент не появилось всплывающее окно с деталями ингредиента'

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_close_ingredient_details_window(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_until_element_visibility(5, MainPageLocators.INGREDIENT_DETAILS_TITLE)
        main_page.click_on_close_button()

        assert main_page.wait_until_element_invisibility(5, MainPageLocators.INGREDIENT_DETAILS_MODAL), \
            'Не удалось закрыть всплывающее окно с деталями ингредиента кликом по крестику'

    @allure.title('Проверка изменения счетчика ингредиента при добавлении его в заказ')
    def test_ingredient_counter_change(self, driver):

        main_page = MainPage(driver)
        original_number = main_page.get_counter_number_of_ingredient_bun()
        main_page.move_bun_to_basket()
        current_number = main_page.get_counter_number_of_ingredient_bun()

        assert original_number < current_number == '2', \
            'При добавлении ингредиента в заказ его счетчик не увеличился'

    @allure.title('Проверка успешного создания заказа')
    def test_successful_order(self, driver, login):

        main_page = MainPage(driver)
        main_page.find_the_element(10, MainPageLocators.INGREDIENT_BUN)
        main_page.move_bun_to_basket()
        main_page.move_filling_to_basket()
        main_page.move_sauce_to_basket()
        main_page.find_the_element(10, MainPageLocators.ORDER_BUTTON)
        main_page.click_on_order_button()
        main_page.wait_until_element_visibility(10, MainPageLocators.ORDER_NUMBER)

        assert main_page.find_the_element(5, MainPageLocators.ORDER_STATUS_TEXT).is_displayed(), \
            'Создание заказа завершилось ошибкой'
