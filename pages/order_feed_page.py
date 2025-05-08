import allure
import curl
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(curl.MAIN_URL + curl.FEED_URL)

    @allure.step("Проверка что открылось окно с деталями заказа")
    def is_window_open(self):
        return int(self.wait_for_element(OrderFeedPageLocators.CARD_ORDER_FEED).text[2:]) == int(
            self.wait_for_element(OrderFeedPageLocators.NUMBER_CARD_ORDER_FEED).text[2:])

    @allure.step("Проверка, что номер заказа из истории есть в ленте")
    def is_order_in_feed(self, order_feed_page, order_number):
        return order_number == int(order_feed_page.wait_for_element(OrderFeedPageLocators.LIST_OF_ORDER).text[2:8])
