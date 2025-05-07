import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.title("Тест если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver):
        lk_page = LkPage(driver)
        with allure.step('Нажать на изображение ингредиента'):
            lk_page.click_on_element(MainPageLocators.INGREDIENT)
        lk_page.main_page_loading_wait()
        with allure.step('Проверяем появление кнопки закрытия окна'):
            assert lk_page.wait_for_element(MainPageLocators.WINDOW_CLOSE_BUTTON)

    @allure.title("Тест всплывающее окно закрывается кликом по крестику")
    def test_close_window_after_click(self, driver):
        lk_page = LkPage(driver)
        with allure.step('Нажать на изображение ингредиента'):
            lk_page.click_on_element(MainPageLocators.INGREDIENT)
        lk_page.main_page_loading_wait()
        with allure.step('Нажать на изображение крестика'):
            lk_page.click_on_element(MainPageLocators.WINDOW_CLOSE_BUTTON)
        with allure.step('Проверяем исчезновение кнопки закрытия окна'):
            assert WebDriverWait(driver, 2).until(EC.invisibility_of_element_located
                                                       (MainPageLocators.WINDOW_CLOSE_BUTTON))

    @allure.title("Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_increase_counter(self, driver):
        lk_page = LkPage(driver)
        with allure.step('Переносим в корзину две булки'):
            lk_page.put_ingredient_into_basket()
        with allure.step('Проверяем значение счетчика'):
            assert int(lk_page.wait_for_element(MainPageLocators.COUNTER).text) == 2

    @allure.title("Тест залогиненный пользователь может оформить заказ")
    def test_take_order(self, driver, login):
        lk_page = LkPage(driver)
        with allure.step('Переносим в корзину две булки'):
            lk_page.put_ingredient_into_basket()
        with allure.step('Нажимаем на кнопку оформить заказ'):
            lk_page.click_on_element(MainPageLocators.BUTTON_TAKE_ORDER)
        with allure.step('Проверяем значение счетчика'):
            assert int(lk_page.wait_for_element(MainPageLocators.ORDER_ID).text) != 0
