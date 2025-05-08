import allure
import curl
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(curl.MAIN_URL + curl.FEED_URL)

    @allure.step("Открыть главную страницу")
    def is_window_open(self):
        return int(self.wait_for_element(OrderFeedPageLocators.CARD_ORDER_FEED).text[2:]) == int(
            self.wait_for_element(OrderFeedPageLocators.NUMBER_CARD_ORDER_FEED).text[2:])