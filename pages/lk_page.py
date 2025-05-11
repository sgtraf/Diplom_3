import allure
from locators.recover_locators import RecoverPageLocators
from pages.base_page import BasePage


class LkPage(BasePage):

    @allure.step('Проверяем наличие слова focused в атрибуте class поля ввода пароля')
    def is_focused_in_passwor_attr(self):
        return 'focused' in self.wait_for_element(RecoverPageLocators.FIELD_PASSWORD).get_attribute('class')
