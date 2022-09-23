from django.test import TestCase, Client


class TestCreateReview(TestCase):

    def test_create_review_should_be_success(self):  # expected success
        c = Client()
        response = c.post("http://127.0.0.1:8000/company_data/review/",
                          data = {
                              "name_user": "asdqwerty",
                              "review": "trolololo"
                          })

        assert response.status_code == 201, f'{response.status_code} should be 201'


