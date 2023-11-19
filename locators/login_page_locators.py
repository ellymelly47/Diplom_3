from selenium.webdriver.common.by import By


class LoginPageLocators:

    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'  # кнопка "Войти" на стр. логина

    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'  # ссылка "Восстановить пароль" на стр. логина
