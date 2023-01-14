
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestDateValidators:

    def test_date_validator_correct(self,):
        response = client.post('/get_form/', json={'test_date': '11.11.2000'})

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"test_date":"DATE"}'

    def test_date_validator_day_incorrect(self):
        response = client.post('/get_form/', json={'test_date': '41.11.2000'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверная дата"}'

    def test_date_validator_month_incorrect(self):
        response = client.post('/get_form/', json={'test_date': '11.41.2000'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверная дата"}'

    def test_iso_date_validator_correct(self):
        response = client.post('/get_form/', json={'test_date': '2000-11-11'})

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"test_date":"DATE"}'

    def test_iso_date_validator_day_incorrect(self):
        response = client.post('/get_form/', json={'test_date': '2000-11-41'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверная дата"}'

    def test_iso_date_validator_month_incorrect(self):
        response = client.post('/get_form/', json={'test_date': '2000-41-11'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверная дата"}'


class TestPhoneValidator:

    def test_phone_correct(self):
        response = client.post('/get_form/',
                               json={'test_phone': '+7 111 111 11 11'})

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"test_phone":"PHONE"}'

    def test_phone_incorrect(self):
        response = client.post('/get_form/',
                               json={'test_phone': '+7 111 111 11 111'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверный номер телефона"}'


class TestEmailValidator:

    def test_email_correct(self):
        response = client.post('/get_form/',
                               json={'test_email': 'email@domen.ru'})

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"test_email":"EMAIL"}'

    def test_email_incorrect(self):
        response = client.post('/get_form/',
                               json={'test_email': 'email@domenru'})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.content.decode() == '{"detail":"Неверный email"}'


class TestTextType:

    def test_text_type_correct(self):
        response = client.post('/get_form/', json={'test_text': 'text'})

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"test_text":"TEXT"}'


class TestFormFinding:

    def test_form_found(self):
        response = client.post('/get_form/',
                               json={
                                   'date': '11.11.2000',
                                   'phone': '+7 111 111 11 11',
                                   'email': 'email@domain.ru',
                                   'text': 'some text',
                               })

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"name":"Form name"}'

    def test_form_found_with_another_field_location(self):
        response = client.post('/get_form/',
                               json={
                                   'date': '11.11.2000',
                                   'phone': '+7 111 111 11 11',
                                   'text': 'some text',
                                   'email': 'email@domain.ru',
                               })

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"name":"Form name"}'

    def test_form_found_with_more_fields_than_in_db(self):
        response = client.post('/get_form/',
                               json={
                                   'date': '11.11.2000',
                                   'phone': '+7 111 111 11 11',
                                   'email': 'email@domain.ru',
                                   'another text': 'some text',
                               })

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == '{"name":"Form name"}'

    def test_form_not_found_correct_response(self):
        response = client.post('/get_form/',
                               json={
                                   'date_not_in_db': '11.11.2000',
                                   'phone': '+7 111 111 11 11',
                                   'email': 'email@domain.ru',
                                   'text': 'some text',
                               })

        assert response.status_code == status.HTTP_200_OK
        assert response.content.decode() == ('{"date_not_in_db":"DATE",'
                                             '"phone":"PHONE",'
                                             '"email":"EMAIL",'
                                             '"text":"TEXT"}')
