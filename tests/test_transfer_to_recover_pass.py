import allure
import curl
from pages.lk_page import LkPage
from locators.lk_locators import LkPageLocators


class TestTransferToRecoverPassword:
    @allure.title("Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transfer_to_recover_password(self, driver):
        # Arrange
        driver = driver('chrome')
        main_page = MainPageSamokat(driver)
        main_page.wait_for_questions_list()
        # Act
        main_page.click_on_element(MainPageLocators.YANDEX_BUTTON)
        main_page.switch_to_next_tab()
        main_page.wait_for_element(MainPageLocators.DZEN_SEARCH)
        # Assert
        assert driver.current_url == curl.DZEN_URL