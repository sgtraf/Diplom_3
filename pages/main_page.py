import allure
import curl
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(curl.MAIN_URL)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()
        ingredient = self.wait_for_element(locator=MainPageLocators.INGREDIENT_0)
        basket = self.wait_for_element(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Сделать заказ')
    def take_order(self):
        with allure.step('Переносим в корзину две булки'):
            self.put_ingredient_into_basket()
        with allure.step('Нажимаем на кнопку оформить заказ'):
            self.click_on_element(MainPageLocators.BUTTON_TAKE_ORDER)