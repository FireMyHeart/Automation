import requests
import random
import string
import allure


class CompanyApi:
    def __init__(self, url):
        self.url = url

    @allure.step("Ввести логин {user} и пароль {pswrd} и получить токен")
    def token(self, user: str = 'flora', pswrd: str = 'nature-fairy') -> str:
        creds = {
            'username': user,
            'password': pswrd
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("Создать через API компанию с рандомным именем")
    def create_random_company(self) -> list:
        charset = string.ascii_letters
        random_name = 'Ann Kotikova random '
        random_description = 'Ann Kotikova random '
        for _ in range(3):
            random_name += random.choice(charset)
            random_description += random.choice(charset)
        company = {
            'name': random_name,
            'description': random_description
        }
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return [resp.json(), random_name, random_description]
