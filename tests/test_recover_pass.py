import allure
import curl
from pages.lk_page import LkPage
from locators.recover_locators import RecoverPageLocators


class TestRecoverPassword:
    @allure.title("Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transfer_to_recover_password(self, driver):
        lk_page = LkPage(driver)
        lk_page.main_page_loading_wait()
        with allure.step('Открыть страницу личного кабинета'):
            lk_page.open(curl.MAIN_URL + curl.LK_URL)
        with allure.step('Нажимаем на текст "Восстановление пароля"'):
            lk_page.click_on_element(RecoverPageLocators.TEXT_RECOVER_PASS)
        lk_page.main_page_loading_wait()

        with allure.step('Проверяем URL страницы'):
            assert lk_page.get_url() == curl.MAIN_URL+curl.FORGOT_PASS_URL

    @allure.title("Тест ввод почты и клик по кнопке «Восстановить»")
    def test_click_on_recover_password(self, driver):
        lk_page = LkPage(driver)
        lk_page.main_page_loading_wait()
        with allure.step('Открыть страницу "Восстановление пароля"'):
            lk_page.open(curl.MAIN_URL + curl.FORGOT_PASS_URL)
        lk_page.main_page_loading_wait()
        with allure.step('Заполняем поле email'):
            lk_page.send_keys_to_input(RecoverPageLocators.FIELD_EMAIL_RECOVER, 'gggg@kkkk.ru')
        with allure.step('Нажимаем на кнопку "Восстановить"'):
            lk_page.click_on_element(RecoverPageLocators.BUTTON_RECOVER_PASS)
        lk_page.main_page_loading_wait()
        lk_page.wait_for_element(RecoverPageLocators.BUTTON_SAVE)

        with allure.step('Проверяем URL страницы'):
            assert lk_page.get_url() == curl.MAIN_URL+curl.RESET_PASS_URL

    @allure.title("Тест клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_click_on_recover_password(self, driver):
        lk_page = LkPage(driver)
        lk_page.main_page_loading_wait()
        with allure.step('Открыть страницу "Восстановление пароля"'):
            lk_page.open(curl.MAIN_URL + curl.FORGOT_PASS_URL)
        lk_page.main_page_loading_wait()
        with allure.step('Заполняем поле email'):
            lk_page.send_keys_to_input(RecoverPageLocators.FIELD_EMAIL_RECOVER, 'gggg@kkkk.ru')
        with allure.step('Нажимаем на кнопку "Восстановить"'):
            lk_page.click_on_element(RecoverPageLocators.BUTTON_RECOVER_PASS)
        lk_page.main_page_loading_wait()
        lk_page.wait_for_element(RecoverPageLocators.BUTTON_SAVE)
        with allure.step('Нажимаем на иконку "Показать пароль"'):
            lk_page.click_on_element(RecoverPageLocators.BUTTON_PASSWORD_VISIBILITY)

        with allure.step('Проверяем наличие слова focused в атрибуте class поля ввода пароля'):
            assert lk_page.is_focused_in_passwor_attr()

