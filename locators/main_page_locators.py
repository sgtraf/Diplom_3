from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    BUTTON_TAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BUTTON_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LABEL_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    INGREDIENT_0 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BASKET = (By.XPATH, "//ul[ @class ='BurgerConstructor_basket__list__l9dp_']")
    COUNTER = (By.XPATH, "//p[ @class ='counter_counter__num__3nue1']")
    ORDER_ID = (By.XPATH, "//h2[@class ='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                          "text_type_digits-large mb-8']")
    LOGO = (By.XPATH, "//div[@class ='AppHeader_header__logo__2D0X2']")
