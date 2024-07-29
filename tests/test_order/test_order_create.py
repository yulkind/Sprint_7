import json
from http import HTTPStatus

import allure
import pytest
import requests

import new_order
from url import Url


@allure.title('Создание заказа с разными вариантами цвета')
@pytest.mark.parametrize('colour', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
def test_create_order_with_black_and_grey_color(colour):
    new_order.NewOrder['colour'] = [colour]
    order = new_order.NewOrder
    headers = {'Content-Type': 'application/json'}
    response = requests.post(Url.URL_ORDER_CREATE, data=order, headers=headers, timeout=5)
    assert response.status_code == HTTPStatus.CREATED
