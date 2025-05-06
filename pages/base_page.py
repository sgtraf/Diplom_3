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