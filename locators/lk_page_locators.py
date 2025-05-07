from selenium.webdriver.common.by import By

class LkPageLocators:

    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    BUTTON_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")