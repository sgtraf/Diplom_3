import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import curl
from locators.main_page_locators import MainPageLocators
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedPageLocators


class TestOrderFeed:
    @allure.title("Тест если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_detailed_window(self, driver):
        order_feed_page = OrderFeedPage(driver)
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.open()
        order_feed_page.main_page_loading_wait()
        with allure.step('Нажать на номер заказа'):
            order_feed_page.click_on_element(OrderFeedPageLocators.CARD_ORDER_FEED)
        order_feed_page.wait_for_element(OrderFeedPageLocators.NUMBER_CARD_ORDER_FEED)
        with allure.step('Проверяем открытие всплывающего окна'):
            assert order_feed_page.is_window_open()

    @allure.title("Тест заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_view_from_history_order(self, driver, order):
        order_number = order
        order_feed_page = OrderFeedPage(driver)
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.open()
        order_feed_page.main_page_loading_wait()
        with allure.step('Проверяем наличие заказа из истории в ленте заказов'):
            assert order_feed_page.is_order_in_feed(order_feed_page, order_number)








