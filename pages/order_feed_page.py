import allure
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Проверка что открылось окно с деталями заказа")
    def is_window_open(self):
        return int(self.wait_for_element(OrderFeedPageLocators.CARD_ORDER_FEED).text[2:]) == int(
            self.wait_for_element(OrderFeedPageLocators.NUMBER_CARD_ORDER_FEED).text[2:])

    @allure.step("Проверка, что номер заказа из истории есть в ленте")
    def is_order_in_feed(self, order_feed_page, order_number):
        return order_number == int(order_feed_page.wait_for_element(OrderFeedPageLocators.LIST_OF_ORDER).text[2:8])

    @allure.step("Ждем появления номера заказа в секции В работе, условие срабатывает, когда вместо текста, "
                 "появляется нужный номер")
    def is_order_number_visible(self, order_number):
        self.wait_for_element_condition(lambda drv: str(order_number) in
                                                               self.wait_for_element
                                                               (OrderFeedPageLocators.IN_WORK).text,
                                                   timeout=15)
