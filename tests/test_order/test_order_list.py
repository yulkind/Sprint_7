import allure
import requests

from url import Url


class TestOrderList:

    @allure.title('Получение списка заказов')
    def test_get_order_list(self):
        response = requests.get(Url.URL_ORDER_CREATE)
        data = response.json()
        assert response.status_code == 200, f'Неожиданный статус ответа: {response.status_code}'
        assert "id" in data['orders'][0], "Поле 'id' отсутствует"
        assert data['orders'][0]['id'] is not None, "Поле 'id' не должно быть None"
