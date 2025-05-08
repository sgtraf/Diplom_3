import allure
import curl
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(curl.MAIN_URL)