from selenium.webdriver.common.by import By


class LkPageLocators:
    TEXT_RECOVER_PASS = (By.XPATH, "//a[text()='Восстановить пароль']")
    BUTTON_RECOVER_PASS = (By.XPATH, "//button[text()='Восстановить']")
    FIELD_EMAIL_RECOVER = ((By.XPATH, "//input[@class='text input__textfield text_type_main-default']"))
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")

