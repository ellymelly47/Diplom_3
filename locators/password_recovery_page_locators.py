from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить" на стр. восстановления пароля

    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить" на стр. восстановления пароля

    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class,"icon-action")]'
    # иконка показа/скрытия пароля в инпуте "Пароль"
