import allure
import curl
from pages.cabinet_page import CabinetPage
from locators.recover_locators import RecoverPageLocators
from locators.main_page_locators import MainPageLocators
from locators.lk_page_locators import LkPageLocators



class TestCabinet:
    @allure.title("Тест переход по клику на «Личный кабинет»")
    def test_transfer_to_cabinet(self, driver, login):
        cabinet_page = login
        cabinet_page.main_page_loading_wait()
        cabinet_page.wait_for_element(MainPageLocators.BUTTON_TAKE_ORDER)
        with allure.step('Нажать на кнопку личного кабинета'):
            cabinet_page.click_on_element(MainPageLocators.BUTTON_CABINET)
        cabinet_page.wait_for_element(LkPageLocators.BUTTON_SAVE)
        with allure.step('Проверяем URL страницы'):
            assert driver.current_url == curl.MAIN_URL+curl.LK_PROFILE

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