from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_LINK = By.XPATH, '//*[@href="/account/profile"]'  # cсылка "Профиль" в личном кабинете

    ORDER_HISTORY_LINK = By.XPATH, '//*[@href="/account/order-history"]'  # cсылка "История заказов" в личном кабинете

    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка "Выход" в личном кабинете

    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'  # статус заказа в Истории заказов в личном кабинете

    ORDER_NUMBER_IN_ORDER_HISTORY = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
    # номер заказа в карточке заказа в Личном кабинете
