from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    BUTTON_TAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BUTTON_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")

