from selenium.webdriver.common.by import By


class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    # кнопка "Войти в аккаунт" на главной стр.

    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер"

    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"

    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    # ингредиаент "Флюоресцентная булка"

    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]'
    # ингредиаент "Говяжий метеорит (отбивная)"

    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'
    # ингредиаент "Соус Spicy-X"

    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]'
    # каунтер ингредиаента "Флюоресцентная булка"

    INGREDIENT_DETAILS_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'
    # заголовок всплывающего окна "Детали ингредиента"

    INGREDIENT_DETAILS_MODAL = By.XPATH, '//*[contains(@class, "contentBox")]'
    # всплывающее окно "Детали ингредиента"

    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'  # корзина заказа бургера

    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'
    # номер заказа во всплывающем окне успешного заказа

    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'
    # дефолтный номер заказа во всплывающем окне успешного заказа (отображается пока не появится актуальный номер заказа)

    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    # заголовок "Ваш заказ начали готовить" во всплывающем окне успешного заказа
