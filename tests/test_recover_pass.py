import allure
import curl
from pages.lk_page import LkPage
from locators.lk_locators import LkPageLocators


class TestRecoverPassword:
    @allure.title("Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transfer_to_recover_password(self, driver):
        # Arrange
        lk_page = LkPage(driver)
        lk_page.main_page_loading_wait()
        # Предвариительно переходим на страницу личного кабинета
        driver.get(curl.MAIN_URL + curl.LK_URL)
        # Act
        lk_page.click_on_element(LkPageLocators.TEXT_RECOVER_PASS)
        lk_page.main_page_loading_wait()
        # Assert
        assert driver.current_url == curl.MAIN_URL+curl.FORGOT_PASS_URL

    @allure.title("Тест ввод почты и клик по кнопке «Восстановить»")
    def test_click_on_recover_password(self, driver):
        # Arrange
        lk_page = LkPage(driver)
        lk_page.main_page_loading_wait()
        # Предвариительно переходим на страницу личного кабинета
        driver.get(curl.MAIN_URL + curl.FORGOT_PASS_URL)
        lk_page.main_page_loading_wait()
        lk_page.send_keys_to_input(LkPageLocators.FIELD_EMAIL_RECOVER, 'gggg@kkkk.ru')
        # Act
        lk_page.click_on_element(LkPageLocators.BUTTON_RECOVER_PASS)
        lk_page.main_page_loading_wait()
        lk_page.wait_for_element(LkPageLocators.BUTTON_SAVE)
        # Assert
        assert driver.current_url == curl.MAIN_URL+curl.RESET_PASS_URL