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


