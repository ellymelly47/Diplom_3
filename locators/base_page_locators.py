from selenium.webdriver.common.by import By


class BasePageLocators:

    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    # инпут "Email" на стр. логина и стр. восстановления пароля

    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'
    # инпут "Пароль" на стр. логина и стр. восстановления пароля

    INPUT_PASSWORD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # инпут "Пароль" в активном состоянии

    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    # крестик закрытия всплывающего окна "Детали ингредиента" / окна с номером заказа / окна с деталями заказа
