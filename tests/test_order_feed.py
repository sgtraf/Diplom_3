import allure
import curl
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedPageLocators
from pages.main_page import MainPage


class TestOrderFeed:
    @allure.title("Тест если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_detailed_window(self, driver):
        order_feed_page = OrderFeedPage(driver)
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.open(curl.MAIN_URL + curl.FEED_URL)
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
            order_feed_page.open(curl.MAIN_URL + curl.FEED_URL)
        order_feed_page.main_page_loading_wait()
        with allure.step('Проверяем наличие заказа из истории в ленте заказов'):
            assert order_feed_page.is_order_in_feed(order_feed_page, order_number)

    @allure.title("Тест при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_create_order_increase_count_total(self, driver, login):
        main_page = MainPage(driver)
        with allure.step('Делаем заказ'):
            main_page.take_order()
        with allure.step('Открыть страницу "Ленты"'):
            main_page.open(curl.MAIN_URL + curl.FEED_URL)
        total_order = main_page.wait_for_element(OrderFeedPageLocators.TOTAL_ORDERS).text
        with allure.step('Открыть страницу главную страницу"'):
            main_page.open(curl.MAIN_URL)
        main_page.main_page_loading_wait()
        with allure.step('Делаем заказ'):
            main_page.take_order()
        with allure.step('Открыть страницу "Ленты"'):
            main_page.open(curl.MAIN_URL + curl.FEED_URL)
        with allure.step('Ждем пока показания счетчика за весь день изменятся'):
            main_page.is_total_count_change(total_order)
        total_order_new = main_page.wait_for_element(OrderFeedPageLocators.TOTAL_ORDERS).text
        with allure.step('Проверяем изменение счетчика'):
            assert total_order_new > total_order

    @allure.title("Тест при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_create_order_increase_count_day(self, driver, login):
        main_page = MainPage(driver)
        with allure.step('Делаем заказ'):
            main_page.take_order()
        with allure.step('Открыть страницу "Ленты"'):
            main_page.open(curl.MAIN_URL + curl.FEED_URL)
        total_order = main_page.wait_for_element(OrderFeedPageLocators.DAY_ORDERS).text
        with allure.step('Открыть страницу главную страницу"'):
            main_page.open(curl.MAIN_URL)
        main_page.main_page_loading_wait()
        with allure.step('Делаем заказ'):
            main_page.take_order()
        with allure.step('Открыть страницу "Ленты"'):
            main_page.open(curl.MAIN_URL + curl.FEED_URL)
        main_page.main_page_loading_wait()
        main_page.wait_for_element(OrderFeedPageLocators.DAY_ORDERS)
        total_order_new = main_page.wait_for_element(OrderFeedPageLocators.DAY_ORDERS).text
        with allure.step('Проверяем изменение счетчика'):
            assert total_order_new > total_order

    @allure.title("Тест после оформления заказа его номер появляется в разделе В работе")
    def test_create_order_increase_in_work(self, driver, order):
        order_number = order
        order_feed_page = OrderFeedPage(driver)
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.open(curl.MAIN_URL + curl.FEED_URL)
        order_feed_page.main_page_loading_wait()
        with allure.step('Ждем появления номера заказа в секции В работе, условие срабатывает, '
                         'когда вместо текста, появляется нужный номер. Сложнейшее условие.'):
            order_feed_page.is_order_number_visible(order_number)
        with allure.step('Проверяем наличие номера заказа в секции "В работе" '):
            assert order_number == int(order_feed_page.wait_for_element(OrderFeedPageLocators.IN_WORK).text)
