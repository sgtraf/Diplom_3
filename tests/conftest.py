import allure
import pytest
import requests
from selenium import webdriver
import curl
from faker import Faker
from pages.lk_page import LkPage
from pages.cabinet_page import CabinetPage
from locators.lk_page_locators import LkPageLocators

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(curl.MAIN_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(curl.MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def registration_user_api():
    fake = Faker()

    email = fake.email(domain='yandex.ru')
    name = fake.first_name()
    password = fake.password()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    register_url = f"{curl.MAIN_URL_API}{curl.CREATE_AND_REGISTRATION_USER_URL}"

    response = requests.post(register_url, data=payload)
    assert response.status_code == 200
    #print(response.json())
    yield payload

    response = requests.delete(curl.MAIN_URL_API+curl.DELETE_USER_URL, headers={"Authorization": response.json()["accessToken"]})
    assert response.status_code == 202


@pytest.fixture(scope="function")
def login(driver, registration_user_api):
    login_page = LkPage(driver)
    with allure.step('Открыть страницу личного кабинета'):
        driver.get(curl.MAIN_URL + curl.LK_URL)
    login_page.send_keys_to_input(LkPageLocators.EMAIL_INPUT, registration_user_api["email"])
    login_page.send_keys_to_input(LkPageLocators.PASSWORD_INPUT, registration_user_api["password"])
    with allure.step('Нажимаем на кнопку "Войти"'):
        login_page.click_on_element(LkPageLocators.BUTTON_ENTER)
    return CabinetPage(driver)