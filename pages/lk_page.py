import allure
from base_page import BasePage
from locators.lk_locators import LkPageLocators

class LkPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()
        ingredient = self.find_element_with_wait(locator=MainPageLocators.FIRST_INGREDIENT)
        basket = self.find_element_with_wait(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)