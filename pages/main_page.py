import allure
from locators.main_page_locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):

    @allure.step("Подождать загрузки страницы")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.BUTTON_ORDER_FEED)