import requests
import random
import string

class CompanyApi:
    def __init__(self, url):
        self.url = url

    def token(self, user='flora', pswrd='nature-fairy'):
        creds = {
        'username':user,
        'password':pswrd
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    def create_random_company(self):
        charset = string.ascii_letters
        random_name = 'Ann Kotikova random '
        random_description = 'Ann Kotikova random '
        for _ in range(3):
            random_name += random.choice(charset)
            random_description += random.choice(charset)
        company = {
        'name':random_name,
        'description':random_description
        }
        # авторизация
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return [resp.json(), random_name, random_description]
