from django.test import TestCase, Client


class TestHomePage(TestCase):

    def test_get_city_list_should_be_success(self):  # expected success
        c = Client()
        response = c.get("http://127.0.0.1:8000/real_estate/city/")

        assert response.status_code == 200, f'{response.status_code} should be 200'


