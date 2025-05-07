from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    BUTTON_TAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BUTTON_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LABEL_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")



