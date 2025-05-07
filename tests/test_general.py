import allure
import curl
from locators.main_page_locators import MainPageLocators
from pages.lk_page import LkPage


class TestGeneral:
    @allure.title("Тест перехода по клику на «Конструктор»")
    def test_transfer_to_construct(self, driver):
        lk_page = LkPage(driver)
        with allure.step('Открыть страницу "Восстановление пароля"'):
            driver.get(curl.MAIN_URL + curl.LK_URL)
        lk_page.main_page_loading_wait()
        with allure.step('Нажать на кнопку Конструктора'):
            lk_page.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        lk_page.wait_for_element(MainPageLocators.BUTTON_CABINET)
        with allure.step('Проверяем наличие надписи "Соберите бургер"'):
            assert lk_page.wait_for_element(MainPageLocators.LABEL_CONSTRUCTOR)

    @allure.title("Тест перехода по клику на «Лента заказов»")
    def test_transfer_to_feed_order(self, driver):
        lk_page = LkPage(driver)
        with allure.step('Нажать на кнопку ленты заказов'):
            lk_page.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)
        lk_page.main_page_loading_wait()
        with allure.step('Проверяем URL страницы'):
            assert driver.current_url == curl.MAIN_URL + curl.FEED_URL
