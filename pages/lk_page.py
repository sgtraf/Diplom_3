import allure
import curl
from pages.base_page import BasePage
from locators.recover_locators import RecoverPageLocators
from locators.main_page_locators import MainPageLocators


class LkPage(BasePage):



    @allure.step('Открыть страницу ЛК')
    def open(self):
        self.driver.get(curl.MAIN_URL + curl.LK_URL)


