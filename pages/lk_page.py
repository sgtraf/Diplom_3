import allure
import curl
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LkPage(BasePage):


    @allure.step('Проверяем исчезновение кнопки закрытия окна')
    def is_close_button_disappear(self):
        return WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located
                                              (MainPageLocators.WINDOW_CLOSE_BUTTON))
