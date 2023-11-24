from selenium.webdriver.common.by import By


class HeaderLocators:

    ACCOUNT_LINK = By.XPATH, '//*[@href="/account"]'  # ссылка на "Личный Кабинет" в хэдере

    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # ссылка "Конструктор" в хэдере

    ORDER_LIST_LINK = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'  # ссылка "Лента Заказов" в хэдере
