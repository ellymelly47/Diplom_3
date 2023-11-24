from selenium.webdriver.common.by import By


class FeedPageLocators:

    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # заголовок "Лента заказов"

    ORDER_NUMBER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'
    # номер заказа из списка "В работе"

    COMPLETED_ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'
    # количество заказов, выполненных за все время

    COMPLETED_ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'
    # количество заказов, выполненных за сегодня

    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в списке "Лента заказа"

    BURGER_CONTENT_TITLE = By.XPATH, '//p[text()="Cостав"]'  # заголовок "Состав" в окне с деталями заказа

    NO_ORDERS_IN_WORK_TITLE = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
    # текст "Все текущие заказы готовы!" под заголовком "В работе"

    ORDER_NUMBER_IN_ORDER_LIST = By.XPATH, '//p[text()="{}"]'  # номер заказа из списка "Лента заказов"
