from http import HTTPStatus

import allure
import pytest
import requests

from new_courier import register_new_courier
from url import Url


class TestCourierLogin:

    @allure.title('Успешный вход в личный кабинет')
    def test_courier_login_with_valid_data(self):
        payload = register_new_courier()
        response = requests.post(Url.URL_COURIER_LOGIN, json=payload)
        assert response.status_code == HTTPStatus.OK, f"Неожиданный статус ответа: {response.status_code}"
        assert 'id' in response.json(), "Поле 'id' не найдено в ответе."

    @allure.title('Неуспешный вход при незаполненном поле логин или пароль')
    @pytest.mark.parametrize('main_fields', [
        {'login': '', 'password': ''},
        {'login': '', 'password': '123'},
        {'login': '123', 'password': ''},
    ])
    def test_courier_login_with_empty_field(self, main_fields):
        response = requests.post(Url.URL_COURIER_LOGIN, data=main_fields)
        assert response.status_code == HTTPStatus.BAD_REQUEST, f"Неожидаемый статуст ответа: {response.status_code}"
        assert response.json().get(
            'message') == 'Недостаточно данных для создания учетной записи', "Сообщение об ошибке некорректно"

    @allure.title('Неуспешный вход с некорректными данными')
    def test_courier_login_with_invalid_data(self):
        payload = {'login': 123, 'password': 123}
        response = requests.post(Url.URL_COURIER_LOGIN, data=payload)
        assert response.status_code == HTTPStatus.NOT_FOUND, f"Неожидаемый статус ответа: {response.status_code}"
        assert response.json().get('message') == 'Учетная запись не найдена', "Сообщение об ошибке некорректно"
