import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)