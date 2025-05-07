import allure
import curl
from pages.cabinet_page import CabinetPage
from locators.recover_locators import RecoverPageLocators
from locators.main_page_locators import MainPageLocators
from locators.lk_page_locators import LkPageLocators
from pages.lk_page import LkPage



class TestCabinet:
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

    @allure.title("Тест перехода в раздел «История заказов»")
    def test_transfer_to_history(self, driver, login):
        cabinet_page = login
        cabinet_page.main_page_loading_wait()
        cabinet_page.wait_for_element(MainPageLocators.BUTTON_TAKE_ORDER)
        with allure.step('Нажать на кнопку личного кабинета'):
            cabinet_page.click_on_element(MainPageLocators.BUTTON_CABINET)
        cabinet_page.wait_for_element(LkPageLocators.BUTTON_SAVE)
        with allure.step('Нажать на кнопку Истории'):
            cabinet_page.click_on_element(LkPageLocators.BUTTON_HISTORY)
        with allure.step('Проверяем URL страницы'):
            assert driver.current_url == curl.MAIN_URL+curl.LK_HISTORY

    @allure.title("Тест выхода из аккаунта")
    def test_logout(self, driver, login):
        cabinet_page = login
        cabinet_page.main_page_loading_wait()
        cabinet_page.wait_for_element(MainPageLocators.BUTTON_TAKE_ORDER)
        with allure.step('Нажать на кнопку личного кабинета'):
            cabinet_page.click_on_element(MainPageLocators.BUTTON_CABINET)
        cabinet_page.wait_for_element(LkPageLocators.BUTTON_SAVE)
        with allure.step('Нажать на кнопку Выход'):
            cabinet_page.click_on_element(LkPageLocators.BUTTON_LOGOUT)
        cabinet_page.main_page_loading_wait()
        cabinet_page.wait_for_element(LkPageLocators.BUTTON_ENTER)
        with allure.step('Проверяем URL страницы'):
            assert driver.current_url == curl.MAIN_URL+curl.LK_URL