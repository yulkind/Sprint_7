from http import HTTPStatus

import allure

from new_courier import *
from url import Url


class TestCourierCreate:
    @allure.title('Успешное создание курьера')
    def test_courier_create_success(self):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(Url.URL_COURIER_CREATE, data=payload)
        assert response.status_code == HTTPStatus.CREATED and response.json() == {"ok": True}

    @allure.title('Неуспешное создание второго одинакового курьера')
    def test_create_duplicate_courier_unsuccessfully(self):
        payload = register_new_courier()
        requests.post(Url.URL_COURIER_CREATE, data=payload)
        response = requests.post(Url.URL_COURIER_CREATE, data=payload)
        assert (response.status_code == HTTPStatus.CONFLICT and
                response.json() == {"message": "Этот логин уже используется"})
