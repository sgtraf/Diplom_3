import allure
from locators.locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):

    @allure.step("Подождать загрузки страницы")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.QUESTIONS)