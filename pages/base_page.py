import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем, пока элемент становится видимым, и кликаем на него')
    def click_on_element(self, sec, element_locator):
        element = WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))
        element.click()

    @allure.step('Ищем элемент, ожидая, пока он становится видимым')
    def find_the_element(self, sec, element_locator):
        element = WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))
        return element

    @allure.step('Ждем, пока указанный элемент станет видимым')
    def wait_until_element_visibility(self, sec, element_locator):
        WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))

    @allure.step('Ждем, пока указанный элемент перестанет быть видимым')
    def wait_until_element_invisibility(self, sec, element_locator):
        return WebDriverWait(self.driver, sec).until(expected_conditions.invisibility_of_element_located(
            element_locator))

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, element_locator):
        return self.driver.find_element(*element_locator).text

    @allure.step('Записываем значение в поле')
    def send_keys_to_element(self, element_locator, value):
        self.driver.find_element(*element_locator).send_keys(value)

    @allure.step('Перемещаемся до элемента и кликаем на него')
    def move_to_element_and_click(self, element_locator):
        element = self.driver.find_element(*element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Перемещаем выбранный элемент до другого элемента')
    def move_element(self, element_locator, to_element_locator):
        element = self.driver.find_element(*element_locator)
        target_element = self.driver.find_element(*to_element_locator)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element, target_element)
