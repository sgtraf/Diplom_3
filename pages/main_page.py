import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

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

    @allure.step('Ждем пока показания счетчика за весь день изменятся')
    def is_total_count_change(self, total_order):
        self.wait_for_element_condition(lambda drv: str(total_order) not in
                                                         self.wait_for_element
                                                         (OrderFeedPageLocators.TOTAL_ORDERS).text,
                                             timeout=10)
