import allure

from models.pages.registration_page import registration_page
from models.user import liza


def test_success_submit():
    with allure.step("Открытие страницы регистрации"):
        registration_page.open()

    with allure.step("Заполнение формы"):
        registration_page.register(liza)

    with allure.step("Проверка успешной отправки формы"):
        registration_page.should_have_registered(liza)
